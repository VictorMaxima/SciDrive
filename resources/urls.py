from django.urls import path, include
from .views import *
urlpatterns = [
    path("paper/create", PaperCreateView.as_view(), name="create_paper" ),
    path("paper/", PaperListView.as_view(), name="paper_list"),
    path("paper/<int:pk>/delete", PaperDeleteView.as_view(), name="paper_delete"),
    path("paper/<int:pk>", PaperUpdateView.as_view(), name="update_paper")
]