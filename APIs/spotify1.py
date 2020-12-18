import requests
import json
from urllib.parse import quote


with open('apikeys.json', 'r') as f:
    keys = json.load(f)

def main():
    userartistquery = quote(str(input("Please enter the artist you're looking for: ")))
    spotifykey = keys['spotify']
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {spotifykey}'
        }
    res = requests.get(f"https://api.spotify.com/v1/search?q={userartistquery}&type=artist", headers=headers)
    if res.status_code != 200:
        raise Exception("ERROR: API Request unsuccesful.")
    data = res.json()
    firstartist = data["artists"]["items"][0]
    fa_name = firstartist["name"]
    fa_followers = firstartist["followers"]["total"]
    fa_URL = firstartist["external_urls"]["spotify"]
    print(f"The artist you queried for is {fa_name}, who has {fa_followers} followers and you can listen to the music here: {fa_URL}")

if __name__ == "__main__":
    main()