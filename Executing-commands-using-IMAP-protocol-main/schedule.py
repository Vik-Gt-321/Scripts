import time
import os
starttime = time.time()
while True:
    # keep looking for new mails every 5 seconds
    os.system("python3 /home/vikram/Documents/Scripts/Mail.py")
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))