import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from .models import SearchResult, Keyword
import time
import random

class Command(BaseCommand):
    help = 'Scrape Google Scholar for search results'

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)
        parser.add_argument('--num_results', type=int, default=10)

    def handle( self, *args, **options):
        print("here")
        query = options['query']
        num_results = options['num_results']
        base_url = "https://www.google.com/scholar"
        params = {
            "q": query,
            "hl": "en"  # Language of the search results
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        new_keyword = Keyword(title=query)
        new_keyword.save()
        page = 0
        while True:
            print("here")
            params['start'] = page * 10
            response = requests.get(base_url, params=params, headers=headers)
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f"Failed to retrieve page {page}. Status code: {response.status_code}"))
                break
            
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('div', class_='gs_ri')
            print(soup)
            
            if not search_results:
                break
            for result in search_results:
                title_tag = result.find('h3', class_='gs_rt')
                if title_tag:
                    title = title_tag.text
                    url = title_tag.a['href'] if title_tag.a else "non"
                    snippet_tag = result.find('div', class_='gs_rs')
                    snippet = snippet_tag.text if snippet_tag else "No snippet available"
                    result = SearchResult(title=title, link=url, snippet=snippet)
                    result.save()
                    new_keyword.results.add(result)
                    
                    
            
            page += 1
            time.sleep(random.uniform(1, 3))  # Be polite and avoid hitting the server too quickly
        
        self.stdout.write(self.style.SUCCESS('Scraping completed'))
