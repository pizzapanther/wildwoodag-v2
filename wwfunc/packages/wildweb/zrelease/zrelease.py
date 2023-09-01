import requests

def main(event, context):
  resp = requests.get("https://api.github.com/repos/pizzapanther/wildwoodag-v2/releases/latest")
  data = resp.json()

  version = data["tag_name"].replace("v", "")
  url = data["assets"][0]["browser_download_url"]

  return {
    "body": {
      "version": version,
      "url": url
    }
  }
