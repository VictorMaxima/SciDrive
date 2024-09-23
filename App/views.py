from django.shortcuts import render
from resources.models import SearchResult, Keyword
from resources.scholar import Command
from resources.pubmed import pub_med
from resources.models import Paper
# Create your views here.

def about(request):
    return render(request, "App/about.html")

def search_paper(query):
    papers = Paper.objects.all().filter(title__contains=query)
    return papers


def index(request):
    q = request.GET.get('q', None)
    items = []
    if q is None or q is "":
        results = None
    elif q is not None:
        keywords = Keyword.objects.filter(title__contains=q)
        if len(keywords) == 0:
            a = Command()
            a.handle(query=q, num_results=80)
            print("command")
        for keyword in keywords:
            print("keyword")
            print(keyword.results)
            for result in keyword.results.all():
                items.append(result)
    return render(request, 'App/index_2.html', {'Results': \
        items})