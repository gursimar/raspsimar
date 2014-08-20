export PATH="$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/home/pi/node-v0.10.2-linux-arm-pi/bin"
date >> ~/raspsimar/logalarm.log
#echo $PATH >> ~/raspsimar/logalarm.log

tvservicepower >> ~/raspsimar/logalarm.log
#tvservice -o
#tvservice -p

for file in ~/media/*.mp4
	do
		echo "Playing file $file" >> ~/raspsimar/logalarm.log
		omxplayer "$file"
		tvservicevolup
		tvservicevolup
	done
date >> ~/raspsimar/logalarm.log
echo "DONE" >> ~/raspsimar/logalarm.log
echo "\r\n\r\n" >> ~/raspsimar/logalarm.log
