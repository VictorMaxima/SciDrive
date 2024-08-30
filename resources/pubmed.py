import requests
from xml.etree import ElementTree
from .models import SearchResult, Keyword

def search_pubmed(query, max_results=30):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': query,
        'retmax': max_results,
        'usehistory': 'y',
        #'api_key': 'YOUR_API_KEY'  # Replace with your NCBI API key, if you have one
    }
    new_keyword = Keyword(title=query)

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    root = ElementTree.fromstring(response.content)
    id_list = [id_elem.text for id_elem in root.findall(".//IdList/Id")]

    return id_list

def fetch_article_details(id_list):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    ids = ','.join(id_list)
    params = {
        'db': 'pubmed',
        'id': ids,
        'retmode': 'xml',
        #'api_key': 'YOUR_API_KEY'  # Replace with your NCBI API key, if you have one
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    root = ElementTree.fromstring(response.content)
    articles = []
    for article in root.findall(".//PubmedArticle"):
        title_elem = article.find(".//ArticleTitle")
        pmid_elem = article.find(".//PMID")
        abstract_elem = article.find(".//Abstract/AbstractText")
        if title_elem is not None and pmid_elem is not None:
            title = title_elem.text
            pmid = pmid_elem.text
            link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            abstract = abstract_elem.text if abstract_elem is not None else "No abstract available"
            articles.append((title, link, abstract))

    return articles

def main(query = "", max_results = "" ):
    
    print(f"Searching PubMed for: {query}")
    id_list = search_pubmed(query, max_results)
    if not id_list:
        print("No articles found.")
        return
    
    print(f"Fetching details for {len(id_list)} articles...")
    articles = fetch_article_details(id_list)
    
    if articles:
        for title, link, abstract in articles:
            new_Result = SearchResult(title=title, link=link, snippet=abstract)
            new_Result.save()
            print(f"Title: {title}")
            print(f"Link: {link}")
            print(f"Abstract: {abstract}")
            print()
pub_med = main
if __name__ == "__main__":
    main()
