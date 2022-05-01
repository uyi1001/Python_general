import requests
temp = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md")
target = temp.text
with open ('download.txt','w') as f:
    f.write(target)

    
