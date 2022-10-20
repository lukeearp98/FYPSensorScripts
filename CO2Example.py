from mqCO2 import *
from mqCO import *
from sendCO2Text import *
from sendCO2Email import *
from sendCOText import *
from sendDataToDB import *
import sys, time

try:
    CO2Trigerred = False
    PreviousTriggeredState = False
    COPreviousTriggeredState = False
    mqCO2 = MQCO2();
    mqCO = MQCO();
    sendDataToDb = insertReading();
    CO2Text = sendCO2Text();
    COText = sendCOText();
    sendCarbonDioxideEmail = sendCO2Email();
    
    while True:
            CO2Perc = mqCO2.MQPercentage()
            COPerc = mqCO.MQPercentage()
            sendDataToDb.insertCO2Reading(CO2Perc["SMOKE"])
            sendDataToDb.insertCOReading(CO2Perc["CO"])
            sys.stdout.write("\r")
            sys.stdout.write("\033[K")
            sys.stdout.write("CO2: %g ppm, CO: %g ppm" % ((CO2Perc["SMOKE"] * 20000), (COPerc["CO"])))
            sys.stdout.flush()
            
            time.sleep(10)
            if ((CO2Perc["SMOKE"]) * 20000) > 1000:
                if PreviousTriggeredState == False:
                    message = CO2Text.createClientMessage()
                    email = sendCarbonDioxideEmail.createEmail()
                PreviousTriggeredState = True
            
            if ((CO2Perc["SMOKE"]) * 20000) <= 1000:
                PreviousTriggeredState = False
            
            if COPerc["CO"] > 70:
                if COPreviousTriggeredState == False:
                    message = COText.createClientMessage()
                COPreviousTriggeredState = True
            
            if COPerc["CO"] <= 70:
                COPreviousTriggeredState = False    
except:
    e = sys.exc_info()[1]
    print("error: %s" % e)