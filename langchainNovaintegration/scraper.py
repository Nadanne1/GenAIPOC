import requests
import json
import time
from typing import List, Dict

class BookDataScraper:
    """Scrape book data from Google Books API and Open Library"""
    
    def __init__(self):
        self.google_books_base = "https://www.googleapis.com/books/v1/volumes"
        self.open_library_base = "https://openlibrary.org"
        
    def search_books(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search for books using Google Books API"""
        try:
            params = {
                'q': query,
                'maxResults': max_results,
                'printType': 'books'
            }
            response = requests.get(self.google_books_base, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            books = []
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                books.append({
                    'title': volume_info.get('title', 'Unknown'),
                    'authors': volume_info.get('authors', []),
                    'publisher': volume_info.get('publisher', 'Unknown'),
                    'published_date': volume_info.get('publishedDate', 'Unknown'),
                    'description': volume_info.get('description', 'No description available'),
                    'page_count': volume_info.get('pageCount', 'Unknown'),
                    'categories': volume_info.get('categories', []),
                    'language': volume_info.get('language', 'Unknown'),
                    'isbn': self._extract_isbn(volume_info.get('industryIdentifiers', [])),
                    'rating': volume_info.get('averageRating', 'No rating'),
                    'ratings_count': volume_info.get('ratingsCount', 0)
                })
            
            return books
        except Exception as e:
            print(f"Error searching books: {e}")
            return []
    
    def get_book_details(self, book_id: str) -> Dict:
        """Get detailed book information"""
        try:
            url = f"{self.google_books_base}/{book_id}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            volume_info = data.get('volumeInfo', {})
            return {
                'title': volume_info.get('title', 'Unknown'),
                'authors': volume_info.get('authors', []),
                'publisher': volume_info.get('publisher', 'Unknown'),
                'published_date': volume_info.get('publishedDate', 'Unknown'),
                'description': volume_info.get('description', 'No description available'),
                'page_count': volume_info.get('pageCount', 'Unknown'),
                'categories': volume_info.get('categories', []),
                'language': volume_info.get('language', 'Unknown'),
                'isbn': self._extract_isbn(volume_info.get('industryIdentifiers', [])),
                'rating': volume_info.get('averageRating', 'No rating'),
                'ratings_count': volume_info.get('ratingsCount', 0)
            }
        except Exception as e:
            print(f"Error getting book details: {e}")
            return {}
    
    def get_open_library_reviews(self, isbn: str) -> List[str]:
        """Get book reviews from Open Library (limited availability)"""
        try:
            url = f"{self.open_library_base}/isbn/{isbn}.json"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Open Library doesn't have reviews, but has ratings and descriptions
            return ["Reviews not available from Open Library API"]
        except Exception as e:
            return [f"Could not fetch reviews: {str(e)}"]
    
    def _extract_isbn(self, identifiers: List[Dict]) -> str:
        """Extract ISBN from industry identifiers"""
        for identifier in identifiers:
            if identifier.get('type') == 'ISBN_13':
                return identifier.get('identifier', 'Unknown')
            elif identifier.get('type') == 'ISBN_10':
                return identifier.get('identifier', 'Unknown')
        return 'Unknown'
    
    def scrape_popular_books(self, categories: List[str] = None) -> Dict[str, List[Dict]]:
        """Scrape popular books from multiple categories"""
        if categories is None:
            categories = ['fiction', 'science fiction', 'mystery', 'romance', 'biography', 
                         'history', 'self-help', 'fantasy', 'thriller', 'classics']
        
        all_books = {}
        for category in categories:
            print(f"Scraping {category} books...")
            books = self.search_books(category, max_results=10)
            all_books[category] = books
            time.sleep(1)  # Be respectful to the API
        
        return all_books
    
    def save_to_json(self, data: Dict, filename: str):
        """Save scraped data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def generate_mock_reviews(self, book_title: str, rating: float) -> List[str]:
        """Generate sample reviews based on rating (since real reviews are hard to get)"""
        if rating == 'No rating' or rating < 3:
            return [
                f"Mixed feelings about {book_title}. Some parts were good, others not so much.",
                f"Expected more from {book_title}. It was okay but didn't meet my expectations.",
                f"{book_title} has potential but falls short in execution."
            ]
        elif rating < 4:
            return [
                f"{book_title} is a solid read. Worth your time if you enjoy the genre.",
                f"Good book overall. {book_title} kept me engaged throughout.",
                f"Enjoyed {book_title}. Not perfect but definitely entertaining."
            ]
        else:
            return [
                f"Absolutely loved {book_title}! Couldn't put it down.",
                f"{book_title} is a masterpiece. Highly recommend to everyone.",
                f"One of the best books I've read. {book_title} exceeded all expectations.",
                f"Outstanding work! {book_title} is a must-read."
            ]

def main():
    """Main function to scrape and save book data"""
    scraper = BookDataScraper()
    
    print("Starting book data scraping...")
    
    # Scrape popular books
    books_data = scraper.scrape_popular_books()
    
    # Save book details
    scraper.save_to_json(books_data, 'data/book_details.json')
    
    # Generate reviews for all books
    reviews_data = {}
    for category, books in books_data.items():
        reviews_data[category] = []
        for book in books:
            rating = book.get('rating', 3.5)
            if rating == 'No rating':
                rating = 3.5
            reviews = scraper.generate_mock_reviews(book['title'], rating)
            reviews_data[category].append({
                'title': book['title'],
                'rating': rating,
                'reviews': reviews
            })
    
    # Save reviews
    scraper.save_to_json(reviews_data, 'data/book_reviews.json')
    
    print("\nScraping complete!")
    print(f"Total categories: {len(books_data)}")
    print(f"Total books scraped: {sum(len(books) for books in books_data.values())}")

if __name__ == "__main__":
    main()
