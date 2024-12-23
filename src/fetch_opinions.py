import requests
import pandas as pd
from config import API_KEY, BASE_URL, DEFAULT_PARAMS, OUTPUT_FILE

# Headers for authentication
HEADERS = {
    "Authorization": f"Token {API_KEY}"
}

def fetch_opinions(params=DEFAULT_PARAMS):
    """
    Fetches opinions from the API based on the given parameters.
    
    Args:
        params (dict): Query parameters for the API request.

    Returns:
        list: A list of opinions (JSON objects).
    """
    opinions = []
    next_url = BASE_URL

    while next_url:
        print(f"Fetching: {next_url}")
        response = requests.get(next_url, headers=HEADERS, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Debugging to ensure API response is correct
            print(f"Response contains {len(data['results'])} results.")
            
            # Check if 'results' exist in the response and add to opinions
            if 'results' in data and data['results']:
                opinions.extend(data['results'])
            else:
                print("No results found in this response. Exiting loop.")
                break
            
            # Update the next URL for pagination
            next_url = data.get('next')
        else:
            print(f"Failed to fetch data: {response.status_code}, {response.text}")
            break

    return opinions

def save_opinions_to_csv(opinions, filename=OUTPUT_FILE):
    """
    Saves the fetched opinions to a CSV file.
    
    Args:
        opinions (list): List of opinions (JSON objects).
        filename (str): Path to the CSV file.
    """
    # Extract relevant fields
    processed_data = [
        {
            "case_name": opinion.get("case_name"),
            "decision_date": opinion.get("decision_date"),
            "court": opinion.get("court"),
            "type": opinion.get("type"),
            "html_with_citations": opinion.get("html_with_citations"),
            "citations": "; ".join(citation.get("cite", "") for citation in opinion.get("citations", [])),
            "url": opinion.get("url"),
        }
        for opinion in opinions
    ]
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(processed_data)
    
    # Debugging: Print the first few rows to verify correctness
    print("Preview of the data to be saved:")
    print(df.head())
    
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def fetch_and_save_opinions():
    """
    High-level function to fetch opinions and save them to a CSV file.
    """
    opinions = fetch_opinions()
    save_opinions_to_csv(opinions)