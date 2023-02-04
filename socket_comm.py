import socketio
import gps_raspi
import csv
from time import sleep

class SocketComm:
    def __init__(self, address, port):
        self.sio = socketio.Client()
        url = "http://" + address + ":" + str(port)
        self.sio.connect(url)
    def send(self, lat, lng):
        message = str(lat) + "," + str(lng)
        self.sio.emit('map message', message)
        # message_bytes = message.encode("utf-8")
        # self.sock.send(message_bytes)
    def __del__(self):
        self.sio.disconnect()

class sampleCSV:
    def __init__(self, filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            self.dataList = [row for row in reader]
        self.index = 0
    def get_data(self):
        data = self.dataList[self.index]
        self.index += 1
        return [data[2], data[3]]
    def judge_over_limit(self):
        if (self.index >= len(self.dataList)):
            return False
        else:
            return True

def update_count():
    with open("number.txt", "r") as f:
        num = int(f.read())
    with open("number.txt", "w") as f:
        f.write(str(num + 1))
    return num

def main():
    deviceName = "raspi01"
    address = "13.114.241.192"
    port = 3000
    sample_filename = "data_from_okayama_to_kokura.csv"
    WAITTIME = 1

    ## construct
    SocketComm01 = SocketComm(address, port)
    CommGPS01 = gps_raspi.CommGPS(deviceName)
    sampleCSV01 = sampleCSV(sample_filename)

    try:
        while(sampleCSV01.judge_over_limit()):
            ## get rowdata from csv
            [latitude, longitude] = sampleCSV01.get_data()
            ## socket communication
            if (float(latitude) == 0):
                pass
            else:
                SocketComm01.send(latitude, longitude)
            ## sleep
            sleep(WAITTIME)
    except KeyboardInterrupt:
        print("ctrl + C")
    finally:
        ## deconstruct
        del SocketComm01
        del CommGPS01
        del sampleCSV01

if __name__ == "__main__":
    main()