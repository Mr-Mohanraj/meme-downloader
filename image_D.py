
import time
import requests
import os

class ImageDownloader:
    def __init__(self) -> None:
        pass
    
    def path_changer():
        import os
        current_path = os.getcwd()
        os.chdir(current_path+"\images")
        current_path = os.getcwd()
        return current_path
    
    def download(links:list):
        link_count = 0
        links_img = []
        for i in links:
            count = time.time()
            count = str(count).split('.')
            count = count[1]
            link_count += 1 
            links_img.append(i)
            url = f"{links_img[link_count - 1]}"
            url = requests.get(url)
            content = url.content
            time.sleep(1)
            print("Downloading...")
            with open(f"E:\PYTHON_practice\images\meme{count}.jpg","wb+") as f:
                f.write(content)
            print("Download complete :)")
            
