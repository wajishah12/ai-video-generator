import sys
import moviepy.editor as mpe

audio = mpe.AudioFileClip(sys.argv[1])
video = mpe.VideoFileClip(sys.argv[2])

final_video = video.set_audio(audio)
final_video.write_videofile("output.mp4")
