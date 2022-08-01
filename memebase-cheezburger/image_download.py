
import os
import time
import requests

class ImageDownloader:
    def __init__(self) -> None:
        pass
    
    def download(links:list):
        try:
            link_count = len(links)
            
            os.chdir("E:\\Python_practice")
            path = os.getcwd() # get current path
            for i in links:
                # here time module using for choose name of the file
                count = time.time()
                count = str(count).split('.')
                count = count[1] # for choose after dot 
                url = f"{i}"
                url = requests.get(url)
                # now content hold the actually image file in byte form
                content = url.content # return bytes
                print("remaining images -->",link_count)
                time.sleep(1)
                print("Downloading...")
                # linux path method is different from windows
                with open(f"{path}\images\memebase-cheezburger\meme{count}.jpg","wb+") as f: # wb+ means write bytes
                    f.write(content)
                print("Download complete :) ")
                print(" ")
                link_count -= 1 # count how many links inside the website(file=images)
        except Exception as error:
            print(f"Error from {__file__}",error)
            

