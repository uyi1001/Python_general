import requests
temp = requests.get("https://static.pandateacher.com/Over%20The%20Rainbow.mp3")
target = temp.content
with open ('download.mp3','wb') as f:
    f.write(target)
