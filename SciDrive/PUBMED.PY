import requests

# Define your base URL for E-utilities
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query, retmax=10):
    """
    Search PubMed with a given query and return a list of PubMed IDs.
    
    :param query: Search query string
    :param retmax: Maximum number of results to return
    :return: List of PubMed IDs
    """
    search_url = BASE_URL + "esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "xml"
    }
    response = requests.get(search_url, params=params)
    response.raise_for_status()
    
    # Parse the XML response to get the list of PubMed IDs
    from xml.etree import ElementTree as ET
    root = ET.fromstring(response.content)
    ids = [id_elem.text for id_elem in root.findall(".//IdList/Id")]
    
    return ids

def fetch_pubmed_details(pmids):
    """
    Fetch detailed information about the PubMed IDs.
    
    :param pmids: List of PubMed IDs
    :return: List of article details
    """
    fetch_url = BASE_URL + "efetch.fcgi"
    ids = ",".join(pmids)
    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml",
        "rettype": "abstract"
    }
    response = requests.get(fetch_url, params=params)
    response.raise_for_status()
    
    # Parse the XML response to extract article details
    from xml.etree import ElementTree as ET
    root = ET.fromstring(response.content)
    articles = []
    
    for docsum in root.findall(".//PubmedArticle"):
        title = docsum.find(".//ArticleTitle").text
        abstract = docsum.find(".//AbstractText").text if docsum.find(".//AbstractText") is not None else ""
        articles.append({"title": title, "abstract": abstract})
    
    return articles

# Example usage
if __name__ == "__main__":
    query = "diabetes"
    pmids = search_pubmed(query, retmax=5)
    articles = fetch_pubmed_details(pmids)
    
    for article in articles:
        pass
        #print(f"Title: {article['title']}")
        #print(f"Abstract: {article['abstract']}")
        #print()
    #print(articles[1])
