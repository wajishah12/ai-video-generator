import sys
from youtube_transcript_api import YouTubeTranscriptApi

video_id = sys.argv[1]
transcript = YouTubeTranscriptApi.get_transcript(video_id)

with open('transcript.txt', 'w') as f:
    for line in transcript:
        f.write(line['text'] + '\n')
