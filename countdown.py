import datetime
import sys
import time
import scrollphat


scrollphat.set_brightness(2)
scrollphat.set_rotate(True) #to sit the zero flat with the usb cable on the top you have to set this as true to rotate the message

while True:
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:&S"))
    birthday = datetime.datetime(YYYY,M,D,0,0) #replace this with the day you want to use - time not important for this application
    print(birthday.strftime("%Y-%m-%d %H:%M:&S"))
    delta = birthday - now 
    print(delta.days)
    #cause we're doing sleeps need +1
    if delta.days + 1 < 1:
        message = "Happy birthday Phina!!!   "
        scroll_delta = 1
    else:
        message = str(delta.days + 1)
        scroll_delta = 0 #because days is a short message don't need to scroll it
    print(message)
    scrollphat.write_string(message)
    length = scrollphat.buffer_len()
    for i in range(length):
        try:
            scrollphat.scroll(delta=scroll_delta)
            time.sleep(0.1)
        except KeyboardInterrupt:
            scrollphat.clear()
            sys.exit(-1)

