# raspi_get_gps

raspberry pi zeroを用いて、GPSモジュールを制御するプログラムとなっている．

## 参考記事

GPSモジュールとRaspberry Piの接続およびプログラムの参考
[https://zenn.dev/kotaproj/books/raspberrypi-tips/viewer/370_kiso_gps](https://zenn.dev/kotaproj/books/raspberrypi-tips/viewer/370_kiso_gps)

crontabでの定期実行

[https://www.raspberrypirulo.net/entry/cron](https://www.raspberrypirulo.net/entry/cron)

秒ごとの実行について

[https://tech.mktime.com/entry/376](https://tech.mktime.com/entry/376)

path について

[https://teratail.com/questions/209388](https://teratail.com/questions/209388)


## プログラムの簡単な説明

[gps_raspi.py](./gps_raspi.py)ファイルは，基本的にPythonスクリプトを実行するとGPSから緯度・経度の情報を取得し，時刻と緯度・経度の情報をCSVファイルに1度書き込むものとなっている．

このコマンドをcron等を用いて定期実行することで，電源投入時からGPSデータを定期取得しCSVに格納してくれる．
