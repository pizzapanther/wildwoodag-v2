import os

import httpx
from filecache import filecache
from user_agent import generate_user_agent

IFRAME = '<iframe class="rumble" width="640" height="360" src="https://rumble.com/embed/v{}/" frameborder="0" allowfullscreen></iframe>'

@filecache(3 * 60)
def main():
  RUMBLE_URL = os.environ['RUMBLE_URL']
  status = 'offline'
  embed = None

  headers = {
    'User-Agent': generate_user_agent()
  }
  response = httpx.get(RUMBLE_URL, headers=headers)
  data = response.json()

  if data['livestreams']:
    live = data['livestreams'][0]
    status = 'live'
    embed = IFRAME.format(live['id'])

  return {
    'body': {'status': status, 'embed': embed},
    'headers': {
      # 'Access-Control-Allow-Origin': '*'
    }
  }
