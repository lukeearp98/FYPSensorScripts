import pyodbc
import datetime
import sys

class insertReading():
    def insertCO2Reading(self, ReadingPPM):
        try:
            conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
            cursor = conn.cursor()
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            sql_text = "INSERT INTO CO2_Readings (DeviceID, ReadingPPM, DateRegistered) VALUES (1," + str(ReadingPPM * 20000) + "," + "'" + now + "'" + ")"
            print(sql_text)
            cursor.execute(sql_text)
            conn.commit()
            conn.close()
        except:
            e = sys.exc_info()[1]
            print("error: %s" % e)
            
    def insertCOReading(self, ReadingPPM):
        try:
            conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
            cursor = conn.cursor()
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            sql_text = "INSERT INTO CO_Readings (DeviceID, ReadingPPM, DateRegistered) VALUES (1," + str(ReadingPPM) + "," + "'" + now + "'" + ")"
            print(sql_text)
            cursor.execute(sql_text)
            conn.commit()
            conn.close()
        except:
            e = sys.exc_info()[1]
            print("error: %s" % e)