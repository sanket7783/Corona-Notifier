import time 
import notify2 
import scrape

# path to notification window icon 
ICON_PATH = "/home/sanket/Desktop/training/Corona\ notifier/icon.ico"


# initialise the d-bus connection 
notify2.init("Corona Notifier") 

# create Notification object 
n = notify2.Notification(None, icon = ICON_PATH) 

# set urgency level 
n.set_urgency(notify2.URGENCY_NORMAL) 

# set timeout for a notification 
n.set_timeout(10000) 

while True:
    
    confirmed,cured,deaths=scrape.getData()

    # update notification data for Notification object 
    n.update("Corona Update", "Confirmed Cases: "+confirmed+"\n"+"Cured: "+cured+"\n"+"Deaths: "+deaths) 

    # show notification on screen 
    n.show() 

    # short delay between notifications 
    time.sleep(3600) 

