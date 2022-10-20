from mq import *
from twilio.rest import Client
import sys, time

class sendCO2Text():
    
    def createClientMessage(self):
        ACCOUNT_SID = 'ACd1cd65da15d96c2208c441a1f4dd7fa0'
        AUTH_TOKEN = '30a6e81f3a740152cb981fb1c31a5c1c'
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
        message = client.messages.create(body='CO2 Reached Unsafe Level', from_='+441873740096', to='+447746103651')
        return message
