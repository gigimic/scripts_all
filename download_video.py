import os
import sys
import pytube 
print('imported pytube')
print(pytube.__version__)
# yt = pytube.YouTube('https://www.youtube.com/watch?v=m0wIU0yvbbs&t=685s')
# yt = pytube.YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
yt = pytube.YouTube('https://www.youtube.com/watch?v=enYITYwvPAQ&t=3s')

print(yt.title)
stream = yt.streams.first()
# stream.download('/path/to/dir/')
stream.download('/home/gigi/Documents')
print('downloaded')
