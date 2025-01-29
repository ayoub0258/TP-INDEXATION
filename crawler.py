import urllib.request
import urllib.robotparser
from urllib.parse import urljoin, urlparse
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import time
import json


def is_allowed_to_crawl(url, user_agent="*"):
    """Vérifie si le crawler est autorisé à accéder à une URL."""
    parsed_url = urlparse(url)
    robots_url = urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", "robots.txt")
    
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except:
        return False  # Si on ne peut pas lire robots.txt, on bloque
    return rp.can_fetch(user_agent, url)


def fetch_html(url):
    """Effectue une requête HTTP pour récupérer le contenu HTML."""
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read().decode("utf-8")
    except HTTPError as e:
        print(f"Erreur HTTP {e.code} pour l'URL {url}: {e.reason}")
    except URLError as e:
        print(f"Erreur de connexion pour l'URL {url}: {e.reason}")
    except Exception as e:
        print(f"Erreur inconnue pour l'URL {url}: {e}")
    return None


def parse_html(html, base_url):
    """Parse le HTML pour extraire le titre, le premier paragraphe et les liens internes."""
    soup = BeautifulSoup(html, "html.parser")
    
    # Titre
    title = soup.title.string.strip() if soup.title else "Titre indisponible"
    
    # Premier paragraphe
    first_paragraph = soup.find("p").get_text(strip=True) if soup.find("p") else " "
    
    # Liens internes
    links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        absolute_url = urljoin(base_url, href)
        if urlparse(absolute_url).netloc == urlparse(base_url).netloc:  # Vérifie si le lien est interne
            links.append(absolute_url)
    
    return title, first_paragraph, links


def prioritize_links(links):
    """Priorise les liens contenant le mot 'product'."""
    product_links = [link for link in links if "product" in link.lower()]
    other_links = [link for link in links if "product" not in link.lower()]
    return product_links + other_links


def crawl(start_url, max_pages):
    """Crawler principal."""
    visited_urls = set()
    to_visit = [start_url]
    crawled_data = []

    while to_visit and len(visited_urls) < max_pages:
        current_url = to_visit.pop(0)
        
        # Vérifie si l'URL a déjà été visitée ou si elle est interdite
        if current_url in visited_urls or not is_allowed_to_crawl(current_url):
            continue
        
        print(f"Crawling: {current_url}")
        html = fetch_html(current_url)
        if not html:
            continue
        
        # Analyse de la page
        title, paragraph, links = parse_html(html, start_url)
        visited_urls.add(current_url)
        crawled_data.append({
            "title": title,
            "url": current_url,
            "first_paragraph": paragraph,
            "links": links,
        })
        
        # Priorisation des liens
        prioritized_links = prioritize_links(links)
        to_visit.extend([link for link in prioritized_links if link not in visited_urls])
        
        # Respecter un délai entre deux requêtes (politesse)
        time.sleep(1)
    
    return crawled_data


def save_results_to_json(data, file_path="results.json"):
    """Enregistre les données crawlées dans un fichier JSON."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Paramètres d'entrée
    start_url = "https://web-scraping.dev/products"  # URL de départ
    max_pages = 50  # Nombre maximum de pages à visiter

    try:
        crawled_data = crawl(start_url, max_pages)
        save_results_to_json(crawled_data)
        print(f"Crawling terminé. Résultats sauvegardés dans 'results.json'.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")