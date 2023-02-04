import csv
import time
import serial
from micropyGPS import MicropyGPS

class CommGPS:
    def __init__(self, devName):
        self.deviceid = devName
        self.uart = serial.Serial('/dev/serial0', 9600, timeout = 10)
        self.my_gps = MicropyGPS(9  , 'dd')
    def get_data(self):
        while(True):
            # tm_last = 0
            sentence = self.uart.readline()
            if len(sentence) > 0:
                for x in sentence:
                    if 10 <= x <= 126:
                        stat = self.my_gps.update(chr(x))
                        if stat:
                            tm = self.my_gps.timestamp
                            timestamp = "{0:02d}:{1:02d}:{2:02.2f}".format(tm[0], tm[1], tm[2])
                            latitude = self.my_gps.latitude[0]
                            longitude = self.my_gps.longitude[0]
                            # tm_now = (tm[0] * 3600) + (tm[1] * 60) + int(tm[2])
                            return [timestamp, latitude, longitude]
                            # if (tm_now - tm_last) >= 10:
                            # print('=' * 20)
                            # print(my_gps.date_string(), tm[0], tm[1], int(tm[2]))
                            # print("latitude:", my_gps.latitude[0], ", longitude:", my_gps.longitude[0])
                            # csv_write("{0:02d}:{1:02d}:{2:02d}".format(tm[0], tm[1], tm[2]), my_gps.latitude[0], my_gps.longitude[0])
                        else:
                            pass


def csv_write(deviceid, timestamp, latitude, longitude):
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([deviceid, timestamp, latitude, longitude])

def main():
    deviceid = "raspi01"
    CommGPS01 = CommGPS(deviceid)
    # gpsモジュールから緯度経度を取得
    [timestamp, latitude, longitude] = CommGPS01.get_data()
    # CSVファイルに書き込み
    csv_write(deviceid, timestamp, latitude, longitude)


def archive():
    # # シリアル通信設定
    # uart = serial.Serial('/dev/serial0', 9600, timeout = 10)
    # # gps設定
    # my_gps = MicropyGPS(9, 'dd')
    flag = 1

    # 10秒ごとに表示
    while (flag):
        tm_last = 0
        sentence = uart.readline()
        if len(sentence) > 0:
            for x in sentence:
                if 10 <= x <= 126:
                    stat = my_gps.update(chr(x))
                    if stat:
                        tm = my_gps.timestamp
                        tm_now = (tm[0] * 3600) + (tm[1] * 60) + int(tm[2])
                        # if (tm_now - tm_last) >= 10:
                        print('=' * 20)
                        print(my_gps.date_string(), tm[0], tm[1], int(tm[2]))
                        print("latitude:", my_gps.latitude[0], ", longitude:", my_gps.longitude[0])
                        csv_write("{0:02d}:{1:02d}:{2:02d}".format(tm[0], tm[1], tm[2]), my_gps.latitude[0], my_gps.longitude[0])
                        flag = 0
                    else:
                        pass


if __name__ == "__main__":
    main()
