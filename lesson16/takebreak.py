import time
import webbrowser

print "the break is starting at" + time.ctime()
for i in range(3):
    time.sleep(60)
    webbrowser.open("https://www.google.com")




