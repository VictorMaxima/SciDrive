from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.edit import (
FormView,
CreateView,
UpdateView,
DeleteView
)
from .models import Paper
# Create your views here.
class PaperListView(LoginRequiredMixin, ListView):
    model = Paper

    def get_queryset(self): 
        return self.model.objects.filter(Publisher=self.request.user)
    
class PaperCreateView(LoginRequiredMixin, CreateView):
    model = Paper
    fields = [
        "title",
        "abstract",
        "picture",
        "file",
        "eISSN",
    ]
    success_url = reverse_lazy("paper_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.Publisher = self.request.user
        obj.save()
        return super().form_valid(form)

class PaperUpdateView(LoginRequiredMixin, UpdateView):
    model = Paper
    fields = [
        "title",
        "abstract",
        "picture",
        "file",
        "eISSN"
    ]
    success_url = reverse_lazy("paper_list")

    def get_queryset(self):
        return self.model.objects.filter(Publisher=self.request.user)

class PaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Paper
    success_url = reverse_lazy("paper_list")

    def get_queryset(self): 
        return self.model.objects.filter(Publisher=self.request.user)