import requests

def fetch_search_results(topic: str, num_results: int = 3, api_key: str = None) -> str:
    if not api_key:
        raise ValueError("SerpAPI API key is required.")

    params = {
        "engine": "google",
        "q": topic,
        "num": num_results,
        "api_key": api_key
    }
    response = requests.get("https://serpapi.com/search", params=params).json()
    results = response.get("organic_results", [])

    snippets = []
    for item in results[:num_results]:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        snippets.append(f"{title}: {snippet} ({link})")

    return "\n\n".join(snippets)
