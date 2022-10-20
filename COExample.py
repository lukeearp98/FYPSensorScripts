from mq import *
from sendCOText import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    COText = sendCOText();
    
    while True:
            perc = mq.MQPercentage()        
            sys.stdout.write("\r")
            sys.stdout.write("\033[K")
            sys.stdout.write("CO: %g ppm" % (perc["CO"]))
            sys.stdout.flush()
            time.sleep(0.1)
            if (perc["CO"]) > 450:
                message = COText.createClientMessage()
                break
    
    print("\r\nMessage has been %s" % message.status)
except:
    e = sys.exc_info()[0]
    print("error: %s" % e)