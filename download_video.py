import os
import sys
from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=m0wIU0yvbbs&t=685s')
yt.streams.all('/home/gigi/Downloads/')