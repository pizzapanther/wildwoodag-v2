import os
import time
import json

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

OAUTH_TOKEN = json.loads(os.environ.get('OAUTH_TOKEN'))
OAUTH_SECRET = json.loads(os.environ.get('OAUTH_SECRET'))


class Channel:
  def __init__(self, channel_id):
    self.channel_id = channel_id

  @property
  def client(self):
    if not getattr(self, '_client', None):
      creds = google.oauth2.credentials.Credentials(**OAUTH_TOKEN)
      self._client = googleapiclient.discovery.build('youtube', 'v3', credentials=creds)

    return self._client

  def find_live(self):
    resp = self.client.search().list(eventType="live", channelId=self.channel_id, part="snippet", maxResults=1, type="video").execute()
    items = resp.get('items')
    if items:
      return items[0]['id']['videoId']

  def get_video(self, vid):
    if not getattr(self, '_video', None):
      resp = self.client.videos().list(part='snippet,status,player', id=vid).execute()
      self._video = resp.get('items')[0]

    return self._video

  def allow_embed(self, vid):
    video = self.get_video(vid)

    if video['status']['embeddable']:
      pass

    else:
      self.client.videos().update(part='status', body={"id": vid, "status": {"embeddable": True}}).execute()
      time.sleep(0.5)
      del self._video


def main(event):
  channel = event.get("channel")
  if not channel:
    return {
      "headers": {
        "Content-Type": "text/plain"
      },
      "statusCode": 404,
      "body": "Channel Required"
    }

  channel = Channel(channel)
  vid = channel.find_live()
  embed = None
  status = 'offline'

  if vid:
    channel.allow_embed(vid)
    data = channel.get_video(vid)
    embed = data['player']['embedHtml']
    status = 'live'

  return {
    'body': {'status': status, 'embed': embed},
    'headers': {
      # 'Access-Control-Allow-Origin': '*'
    }
  }
