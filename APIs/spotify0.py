import requests
import json


with open('apikeys.json', 'r') as f:
    keys = json.load(f)

def main():
    spotifykey = keys['spotify']
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {spotifykey}'
        }
    res = requests.get("https://api.spotify.com/v1/search?q=flume&type=artist", headers=headers)
    if res.status_code != 200:
        raise Exception("ERROR: API Request unsuccesful.")
    data = res.json()
    print(data)
    with open('flumeQueryResponse.json', 'w') as newfile:
        json.dump(data, newfile)



if __name__ == "__main__":
    main()
