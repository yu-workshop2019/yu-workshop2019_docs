#!/bin/bash
#automatically starts mepg-streamer(Raspberry Pi x WebCam Live Camera system)

export LD_LIBRARY_PATH=/opt/mjpg-streamer

#the following line is for normal quality (VGA:640x480 15fps)
#sudo /opt/mjpg-streamer/mjpg_streamer -i "/opt/mjpg-streamer/input_uvc.so -f 15 -r VGA -d /dev/video0 -y -l "off"  -n" -o "/opt/mjpg-streamer/output_http.so -w /opt/mjpg-streamer/www -p 9000 -c pi:raspberry" &

#the following line is for normal quality (VGA:640x480 30fps)
#sudo /opt/mjpg-streamer/mjpg_streamer -i "/opt/mjpg-streamer/input_uvc.so -f 30 -r VGA -d /dev/video0 -y -l "off"  -n" -o "/opt/mjpg-streamer/output_http.so -w /opt/mjpg-streamer/www -p 9000 -c pi:raspberry" &

#the following line is without password
sudo /opt/mjpg-streamer/mjpg_streamer -i "/opt/mjpg-streamer/input_uvc.so -f 30 -r VGA -d /dev/video0 -y -l "off"  -n" -o "/opt/mjpg-streamer/output_http.so -w /opt/mjpg-streamer/www -p 9000" &

#the following line is for high quality (SXGA:1280x1024 9fps)
#sudo /opt/mjpg-streamer/mjpg_streamer -i "/opt/mjpg-streamer/input_uvc.so -f 9  -r SXGA -d /dev/video0 -y -l "off"  -n" -o "/opt/mjpg-streamer/output_http.so -w /opt/mjpg-streamer/www -p 9000 -c pi:raspberry" &

#reasonable
#sudo /opt/mjpg-streamer/mjpg_streamer -i "/opt/mjpg-streamer/input_uvc.so -f 30  -r 1270x720 -d /dev/video0 -y -l "off"  -n" -o "/opt/mjpg-streamer/output_http.so -w /opt/mjpg-streamer/www -p 9000 -c pi:raspberry" &

#too high resolution
#sudo /opt/mjpg-streamer/mjpg_streamer -i "/opt/mjpg-streamer/input_uvc.so -f 30  -r 1920x1080 -d /dev/video0 -y -l "off"  -n" -o "/opt/mjpg-streamer/output_http.so -w /opt/mjpg-streamer/www -p 9000 -c pi:raspberry" &
