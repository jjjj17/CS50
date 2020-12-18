import requests

def main():
    res = requests.get("https://data.fixer.io/api/latest")
    if res.status_code != 200:
        raise Exception("ERROR: API Request unsuccesful.")
    data = res.json()
    print(data)


if __name__ == "__main__":
    main()


### DEPRECATED CODE BECAUSE FIXER.IO REQUIRES API KEY NOW, SEE spotify0.py ###