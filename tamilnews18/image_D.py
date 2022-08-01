
import time
import requests

class ImageDownloader:
    def __init__(self) -> None:
        pass
    
    def download(links:list):
        link_count = len(links)
        for i in links:
            # for file name 
            count = time.time()
            count = str(count).split('.')
            count = count[1]
            
            # for get image source from the website
            url = f"{i}"
            url = requests.get(url)
            content = url.content
            print("Remaining Image file -->",link_count)
            time.sleep(1)
            print("Downloading...")
            #for write the file inside the list
            with open(f".\images\meme{count}.jpg","wb+") as f:
                f.write(content)
            print("Download complete :)")
            link_count -= 1 
