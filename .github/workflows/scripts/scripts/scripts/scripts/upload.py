import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# Replace with your credentials
creds = Credentials.from_authorized_user_file('token.json')

youtube = build('youtube', 'v3', credentials=creds)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Your Video Title",
            "description": "Your video description"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload(sys.argv[1])
)
response = request.execute()
