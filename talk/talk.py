#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from datetime import datetime
import sys

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/miku/miku.htsvoice']
    #htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','output_voice.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','output_voice.wav']
    wr = subprocess.Popen(aplay)
    wr.wait()

def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    jtalk(text)

def recite(fname):
	f = open(fname, "r")
	text = f.read()
	f.close()
	jtalk(text)


def main():
	args = sys.argv
	#jtalk(args[1])
	#say_datetime()
	recite("./serif.txt")


if __name__ == '__main__':
    main()
