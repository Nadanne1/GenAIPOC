import requests
import json
import time
import os
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MovieDataScraper:
    """Scrape movie data from OMDB API"""
    
    def __init__(self):
        self.omdb_base = "http://www.omdbapi.com/"
        self.api_key = os.getenv('OMDB_API_KEY')
        if not self.api_key:
            raise ValueError("OMDB_API_KEY not found in environment variables")
        
    def search_movies(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search for movies using OMDB API"""
        try:
            params = {
                'apikey': self.api_key,
                's': query,
                'type': 'movie'
            }
            response = requests.get(self.omdb_base, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            movies = []
            if data.get('Response') == 'True':
                search_results = data.get('Search', [])
                # Limit results to max_results
                for item in search_results[:max_results]:
                    # Get detailed info for each movie
                    movie_details = self.get_movie_details(item.get('imdbID'))
                    if movie_details:
                        movies.append(movie_details)
                    time.sleep(0.1)  # Small delay between requests
            
            return movies
        except Exception as e:
            print(f"Error searching movies: {e}")
            return []
    
    def get_movie_details(self, imdb_id: str) -> Dict:
        """Get detailed movie information with streaming data"""
        try:
            params = {
                'apikey': self.api_key,
                'i': imdb_id,
                'plot': 'full'
            }
            response = requests.get(self.omdb_base, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('Response') == 'True':
                movie_data = {
                    'title': data.get('Title', 'Unknown'),
                    'director': data.get('Director', 'Unknown'),
                    'cast': [actor.strip() for actor in data.get('Actors', '').split(',') if actor.strip()],
                    'studio': data.get('Production', 'Unknown'),
                    'release_date': data.get('Released', 'Unknown'),
                    'description': data.get('Plot', 'No description available'),
                    'runtime_minutes': self._parse_runtime(data.get('Runtime', '0')),
                    'genres': [genre.strip() for genre in data.get('Genre', '').split(',') if genre.strip()],
                    'language': data.get('Language', 'Unknown'),
                    'imdb_id': data.get('imdbID', 'Unknown'),
                    'rating': self._parse_rating(data.get('imdbRating', 'N/A')),
                    'ratings_count': self._parse_votes(data.get('imdbVotes', '0')),
                    'box_office': data.get('BoxOffice', 'Unknown'),
                    'awards': data.get('Awards', 'None')
                }
                
                # Add streaming data (OMDB doesn't provide this, so we'll generate realistic mock data)
                streaming_data = self._generate_streaming_data(movie_data)
                movie_data.update(streaming_data)
                
                return movie_data
            return {}
        except Exception as e:
            print(f"Error getting movie details: {e}")
            return {}
    
    def _parse_runtime(self, runtime_str: str) -> int:
        """Parse runtime string to minutes"""
        try:
            # Runtime comes as "148 min" or similar
            return int(runtime_str.split()[0]) if runtime_str and runtime_str != 'N/A' else 0
        except:
            return 0
    
    def _parse_rating(self, rating_str: str) -> float:
        """Parse IMDb rating string to float"""
        try:
            return float(rating_str) if rating_str and rating_str != 'N/A' else 0.0
        except:
            return 0.0
    
    def _parse_votes(self, votes_str: str) -> int:
        """Parse IMDb votes string to integer"""
        try:
            # Votes come as "1,234,567" with commas
            return int(votes_str.replace(',', '')) if votes_str and votes_str != 'N/A' else 0
        except:
            return 0
    
    def _generate_streaming_data(self, movie_data: dict) -> dict:
        """Generate realistic streaming availability data"""
        import random
        
        title = movie_data.get('title', '')
        year = self._extract_year(movie_data.get('release_date', ''))
        genres = movie_data.get('genres', [])
        studio = movie_data.get('studio', '').lower()
        rating = movie_data.get('rating', 0)
        
        # Available streaming platforms
        all_platforms = ['Netflix', 'Amazon Prime', 'Hulu', 'Disney+', 'HBO Max', 'Apple TV']
        available_platforms = []
        rental_platforms = []
        
        # Studio-based logic
        if 'disney' in studio or 'pixar' in studio or any(genre.lower() in ['animation', 'family'] for genre in genres):
            if random.random() > 0.3:  # 70% chance
                available_platforms.append('Disney+')
        
        if 'warner' in studio or 'hbo' in studio:
            if random.random() > 0.4:  # 60% chance
                available_platforms.append('HBO Max')
        
        # Year-based logic
        current_year = 2024
        if year >= 2020:  # Recent movies
            # Newer movies more likely on rental platforms
            rental_platforms.extend(random.sample(['Amazon Prime', 'Apple TV', 'Hulu'], 
                                                random.randint(1, 2)))
            # Less likely on subscription platforms
            if random.random() > 0.7:  # 30% chance
                available_platforms.append(random.choice(['Netflix', 'Hulu']))
        
        elif year >= 2010:  # Mid-range movies
            # Good chance on major platforms
            available_platforms.extend(random.sample(['Netflix', 'Amazon Prime'], 
                                                   random.randint(1, 2)))
            
        else:  # Older movies
            # More widely available
            available_platforms.extend(random.sample(['Netflix', 'Amazon Prime', 'Hulu'], 
                                                   random.randint(2, 3)))
        
        # Rating-based logic - higher rated movies more available
        if rating >= 8.0:
            if random.random() > 0.5:  # 50% chance to add another platform
                remaining = [p for p in all_platforms if p not in available_platforms]
                if remaining:
                    available_platforms.append(random.choice(remaining))
        
        # Ensure some variety and remove duplicates
        available_platforms = list(set(available_platforms))
        rental_platforms = list(set(rental_platforms))
        
        # Ensure at least one option exists
        if not available_platforms and not rental_platforms:
            available_platforms.append(random.choice(['Netflix', 'Amazon Prime']))
        
        # Determine unavailable platforms
        not_available = [p for p in all_platforms 
                        if p not in available_platforms and p not in rental_platforms]
        
        return {
            'streaming_platforms': available_platforms,
            'rental_platforms': rental_platforms,
            'not_available': not_available
        }
    
    def _extract_year(self, date_str: str) -> int:
        """Extract year from release date string"""
        try:
            # Handle various date formats: "18 Jun 1993", "1993", "Jun 1993"
            import re
            year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
            return int(year_match.group()) if year_match else 2000
        except:
            return 2000
    
    def scrape_popular_movies(self, categories: List[str] = None) -> Dict[str, List[Dict]]:
        """Scrape popular movies from multiple categories"""
        if categories is None:
            categories = ['action', 'comedy', 'drama', 'sci-fi', 'thriller', 
                         'romance', 'horror', 'adventure', 'animation', 'crime']
        
        all_movies = {}
        for category in categories:
            print(f"Scraping {category} movies...")
            movies = self.search_movies(category, max_results=10)
            all_movies[category] = movies
            time.sleep(1)  # Be respectful to the API
        
        return all_movies
    
    def save_to_json(self, data: Dict, filename: str):
        """Save scraped data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def generate_mock_reviews(self, movie_title: str, rating: float) -> List[str]:
        """Generate sample reviews based on rating (since real reviews are hard to get)"""
        if rating == 0 or rating < 5.0:
            return [
                f"Mixed feelings about {movie_title}. Some scenes were good, others not so much.",
                f"Expected more from {movie_title}. It was okay but didn't meet my expectations.",
                f"{movie_title} has potential but falls short in execution."
            ]
        elif rating < 7.0:
            return [
                f"{movie_title} is a solid watch. Worth your time if you enjoy the genre.",
                f"Good movie overall. {movie_title} kept me engaged throughout.",
                f"Enjoyed {movie_title}. Not perfect but definitely entertaining."
            ]
        else:
            return [
                f"Absolutely loved {movie_title}! Couldn't look away.",
                f"{movie_title} is a masterpiece. Highly recommend to everyone.",
                f"One of the best movies I've seen. {movie_title} exceeded all expectations.",
                f"Outstanding work! {movie_title} is a must-watch."
            ]

def main():
    """Main function to scrape and save movie data"""
    scraper = MovieDataScraper()
    
    print("Starting movie data scraping...")
    
    # Scrape popular movies
    movies_data = scraper.scrape_popular_movies()
    
    # Save movie details
    scraper.save_to_json(movies_data, 'data/movie_details.json')
    
    # Generate reviews for all movies
    reviews_data = {}
    for category, movies in movies_data.items():
        reviews_data[category] = []
        for movie in movies:
            rating = movie.get('rating', 5.0)
            if rating == 0:
                rating = 5.0
            reviews = scraper.generate_mock_reviews(movie['title'], rating)
            reviews_data[category].append({
                'title': movie['title'],
                'rating': rating,
                'reviews': reviews
            })
    
    # Save reviews
    scraper.save_to_json(reviews_data, 'data/movie_reviews.json')
    
    print("\nScraping complete!")
    print(f"Total categories: {len(movies_data)}")
    print(f"Total movies scraped: {sum(len(movies) for movies in movies_data.values())}")

if __name__ == "__main__":
    main()
