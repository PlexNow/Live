#!/usr/bin/env python3

import requests
import os
import sys

windows = False
if "win" in sys.platform:
    windows = True

def grab(url):
    response = s.get(url, timeout=15).text
    if ".m3u8" not in response:
        response = requests.get(url).text
        if ".m3u8" not in response:
            if windows:
                print('https://raw.githubusercontent.com/PlexNow/Live/main/Info.mp4')
                return
            os.system(f"curl '{url}' > temp.txt")
            response = "".join(open("temp.txt").readlines())
            if ".m3u8" not in response:
                print('https://raw.githubusercontent.com/PlexNow/Live/main/Info.mp4')
                return
    end = response.find(".m3u8") + 5
    tuner = 100
    while True:
        if "https://" in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find("https://")
            end = link.find(".m3u8") + 5
            break
        else:
            tuner += 5
    streams = s.get(link[start:end]).text.split("#EXT")
    hd = streams[-2].strip()
    st = hd.find("http")
    print(hd[st:].strip())

print("#EXTM3U")
print("#EXT-X-STREAM-INF:BANDWIDTH=2969452")
s = requests.Session()
with open("../information/ZKL0D310Jd0F7k4dm9o13sL7pDGD8sIIq510p0928JpQ2914912347129866029275628957gu389gii48t8g92oig84y6hy8h83oguh6re9i3orfit4urofg4uurur7salk3jofj39ajlij09409jbhbdfj9d489tjlijhiojh598efjm914D.txt") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("~~"):
            continue
        if not line.startswith("https:"):
            line = line.split("|")
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            grab(line)

if "temp.txt" in os.listdir():
    os.system("rm temp.txt")
    os.system("rm watch*")