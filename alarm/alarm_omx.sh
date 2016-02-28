export PATH="$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/home/pi/node-v0.10.2-linux-arm-pi/bin"
date >> ~/raspsimar/logalarm.log
#echo $PATH >> ~/raspsimar/logalarm.log

tvservicepower >> ~/raspsimar/logalarm.log
#tvservice -o
#tvservice -p

omxplayer ~/media/kirtan/kirtan_na_mai_hindu_na_musalman.mp4

date >> ~/raspsimar/logalarm.log
echo "DONE" >> ~/raspsimar/logalarm.log
echo "\r\n\r\n" >> ~/raspsimar/logalarm.log
#this switch off does not work
tvservicepower >> ~/raspsimar/logalarm.log
