# Configuration for the Opinions Scraper

# API Key for the CourtListener API. This will have to be hidden better. Perhaps through axios or secondary file
API_KEY = "5408ae53f88d25cb0814abb4f063f91d8df249eb"

# Endpoint
BASE_URL = "https://www.courtlistener.com/api/rest/v4/opinions/"

# Default parameters for API requests. This will need some tweeking to manage pull size
DEFAULT_PARAMS = {
    "type": "020lead",  # Use the correct value for Lead Opinion
    "decision_date_min": "2022-11-01",  # Adjust date range as needed
    "decision_date_max": "2023-01-01",
    "page_size": 10  # Maximum results per page
}

# Output file path for saving opinions
OUTPUT_FILE = "../data/opinions.csv"
