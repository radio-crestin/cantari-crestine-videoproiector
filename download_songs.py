import requests
import json
import os
import re

def download_raw_songs():
    print("Creating data directory...")
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    url = "https://cantari-crestine.com/json-data/texts.json?ILrPyVo"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'cache-control': 'no-cache',
    }

    print("Downloading songs data...")
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # Save response to JSON file
    with open('data/raw_songs.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=2)
    
    return response.json()

def process_songs(raw_data):
    processed_songs = []
    
    category_names = {
        'CC': 'Carte Cântari BER',
        'CT': 'Cântari tineret',
        'Cor': 'Cântari cor',
        'J': 'Jubilate',
        'CB': 'Cântari ale Bisericilor de peste veacuri'
    }
    
    for category in category_names.keys():
        for idx, song_text in enumerate(raw_data[category], 1):
            if not song_text.strip():
                continue
                
            # Split into slides based on double newlines
            slides = [slide.strip() for slide in song_text.split('\n\n') if slide.strip()]
            
            # Get title from first line, removing any leading and trailing non-letters except '?' and keeping diacritics
            first_line = slides[0].split('\n')[0]
            title = re.sub(r'^[^a-zA-ZăâîșțĂÂÎȘȚ]+', '', first_line).strip()  # Remove leading non-letters
            title = re.sub(r'[^a-zA-ZăâîșțĂÂÎȘȚ\?]+$', '', title).strip()  # Remove trailing non-letters except '?'
            
            # Clean filename for URL
            clean_title = title
            filename = "".join(c for c in clean_title if c.isalnum() or c in (' ', '-', '_', '.'))
            filename = f"{filename}.pptx"
            
            # Construct GitHub URL
            github_url = f"https://raw.githubusercontent.com/radio-crestin/cantari-crestine-videoproiector/main/data/pptx/{category_names[category]}/{filename}"
            
            song = {
                'pk': f"{category}-{idx}",
                'type': category_names[category],
                'original_type_abvr': category,
                'type_abvr': category.upper(),
                'title': title,
                'slides': slides,
                'pptx_url': github_url
            }
            processed_songs.append(song)
    
    return processed_songs

def save_processed_songs(songs):
    with open('data/songs.json', 'w', encoding='utf-8') as f:
        json.dump(songs, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print("Starting song download process...")
    raw_data = download_raw_songs()
    print("Processing songs data...")
    processed_songs = process_songs(raw_data)
    print("Saving processed songs...")
    save_processed_songs(processed_songs)
    print("Done!")
