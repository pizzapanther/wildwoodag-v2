import requests

from filecache import filecache

@filecache(5 * 60)
def main():
  resp = requests.get("https://api.github.com/repos/pizzapanther/wildwoodag-v2/releases/latest")
  data = resp.json()
  print("retrieved new data")

  version = data["tag_name"].replace("v", "")
  url = data["assets"][0]["browser_download_url"]

  return {
    "body": {
      "version": version,
      "url": url
    }
  }
