import time
import sys
from urllib.request import urlretrieve

def progress(downloaded, block_size, total_size):
    global download_size
    download_size = total_size
    completed = round(downloaded / (total_size//block_size) * 100)
    sys.stdout.write("\r|" + "█" * completed + " " * (100-completed) + "|{}%".format(completed),end="")

def download_bar(url,filename):
    start = time.time()
    try:
        urlretrieve(url,filename,progress)
    except:
        sys.stderr.write("An unknown error occured.")
        exit(0)
    end = time.time()
    print("\n",end="")
    time_taken = end - start
    download_speed = round(download_size/(time_taken*1024),2)
    if download_speed > 1024:
        sys.stdout.write("Downloaded in " + str(round(time_taken,2)) + "s (" + str(download_speed/1024) + " MB/s)" + "\n")
    if download_speed < 1024:
        sys.stdout.write("Downloaded in " + str(round(time_taken,2)) + "s (" + str(download_speed) + " kB/s)" + "\n")
    if download_speed < 1:
        sys.stdout.write("Downloaded in " + str(round(time_taken,2)) + "s (" + str(download_speed*1024) + " B/s)" + "\n")
