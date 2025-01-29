import unittest
from unittest.mock import patch, MagicMock
from crawler import fetch_html, parse_html, prioritize_links, is_allowed_to_crawl

class TestCrawler(unittest.TestCase):

    @patch('crawler.urllib.request.urlopen')
    def test_fetch_html_http_error(self, mock_urlopen):
        """Test de la fonction fetch_html pour gérer une erreur HTTP"""
        mock_urlopen.side_effect = Exception("HTTP Error")
        
        url = "https://web-scraping.dev/products"
        result = fetch_html(url)
        
        self.assertIsNone(result)

    def test_parse_html(self):
        """Test de la fonction parse_html"""
        html = "<html><head><title>Test Page</title></head><body><p>Test paragraph</p><a href='https://web-scraping.dev/products'>Product Link</a></body></html>"
        base_url = "https://web-scraping.dev"
        
        title, paragraph, links = parse_html(html, base_url)
        
        self.assertEqual(title, "Test Page")
        self.assertEqual(paragraph, "Test paragraph")
        self.assertEqual(links, ["https://web-scraping.dev/products"])

    def test_prioritize_links(self):
        """Test de la fonction prioritize_links"""
        links = [
            "https://web-scraping.dev/product/1",
            "https://web-scraping.dev/about",
            "https://web-scraping.dev/product/2"
        ]
        
        prioritized = prioritize_links(links)
        
        self.assertEqual(prioritized[0], "https://web-scraping.dev/product/1")
        self.assertEqual(prioritized[1], "https://web-scraping.dev/product/2")
        self.assertEqual(prioritized[2], "https://web-scraping.dev/about")

    def test_is_allowed_to_crawl(self):
        """Test de la fonction is_allowed_to_crawl"""
        # En supposant que le site est autorisé à être crawlé
        url = "https://web-scraping.dev/products"
        result = is_allowed_to_crawl(url)
        
        self.assertTrue(result)
        
        # URL invalide, pas autorisée
        url = "ftp://web-scraping.dev/products"
        result = is_allowed_to_crawl(url)
        
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
