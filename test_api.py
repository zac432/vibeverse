import requests

access_token = "p_o14Y47yGd0SBvmPdGIAS16IFclamd1UZ9IyzRZhb7yrQPoCcrLEYkY3IQRz-Ap"
headers = {"Authorization": f"Bearer {access_token}"}
query = "Adele Hello"
url = f"https://api.genius.com/search?q={query}"

response = requests.get(url, headers=headers)
data = response.json()

for hit in data["response"]["hits"]:
    song = hit["result"]
    print(f"Title: {song['full_title']}")
    print(f"Artist: {song['artist_names']}")
    print(f"Lyrics URL: https://genius.com{song['path']}")
    print(f"Release Date: {song.get('release_date_for_display', 'N/A')}")
    print("-" * 40)
