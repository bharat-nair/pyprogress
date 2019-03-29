import time
import sys
from urllib.request import urlretrieve

def progress(downloaded, block_size, total_size):
    global download_size
    download_size = total_size
    completed = round(downloaded / (total_size//block_size) * 100)
    sys.stdout.write("\r|" + "█" * completed + " " * (100-completed) + "|{}%".format(completed))
    
def simple_bar(dur=10,bar="█"):

    for i in range(dur+1):
        perc = str(round((i/dur)*100))
        sys.stdout.write("\r|" + bar * i + " " * (dur-i) + "|{}%".format(perc))
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n")

def download_bar(url,filename):
    start = time.time()
    urlretrieve(url,filename,progress)
    end = time.time()
    sys.stdout.write("\n")
    time_taken = end - start
    download_speed = round(download_size/(time_taken*1000),2)
    sys.stdout.write("Downloaded in " + str(round(time_taken,2)) + "s (" + str(download_speed) + " kB/s)" + "\n")


download_bar("ftp://speedtest:speedtest@ftp.otenet.gr/test1Mb.db","test1.db")

# simple_bar(50,'.')
