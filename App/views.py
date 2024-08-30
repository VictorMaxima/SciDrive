from django.shortcuts import render
from resources.models import SearchResult, Keyword
from resources.SCHOLAR import Command
from resources.pubmed import pub_med
# Create your views here.
def index(request):
    q = request.GET.get('q', None)
    items = []
    if q is None or q is "":
        results = None
    elif q is not None:
        keywords = Keyword.objects.filter(title__contains=q)
        if len(keywords) == 0:
            Command.handle(query=q, num_results=80)
            pub_med(query=q, max_results=80)
            print("command")
        for keyword in keywords:
            print("keyword")
            for result in keyword.results.all():
                items.append(result)
    return render(request, 'App/index_2.html', {'Results': \
        items})