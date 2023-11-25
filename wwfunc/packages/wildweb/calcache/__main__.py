import requests

from filecache import filecache

@filecache(10 * 60)
def main():
  resp = requests.get("https://calendar.google.com/calendar/ical/62da059a43acfa2924e50e6aaa43e3aed3728f7eda51af7d7a43f0313404e09c%40group.calendar.google.com/public/basic.ics")
  return {
    "headers": {
      "Content-Type": "text/calendar"
    },
    "statusCode": 200,
    "body": resp.text
  }
