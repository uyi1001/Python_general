import requests
temp = requests.get("https://res.pandateacher.com/2019-01-12-15-29-33.png")
target = temp.content
with open ('download.jpg','wb') as f:
    f.write(target)
