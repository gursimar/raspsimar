export PATH="$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/home/pi/node-v0.10.2-linux-arm-pi/bin"
date >> ~/raspsimar/logalarm.log
#echo $PATH >> ~/raspsimar/logalarm.log


echo "on 0" | cec-client -s
echo "as" | cec-client -s
omxplayer ~/media/kirtan/kirtan_na_mai_hindu_na_musalman.mp4
echo "standby 0" | cec-client -s

date >> ~/raspsimar/logalarm.log
echo "DONE" >> ~/raspsimar/logalarm.log
echo "\r\n\r\n" >> ~/raspsimar/logalarm.log
