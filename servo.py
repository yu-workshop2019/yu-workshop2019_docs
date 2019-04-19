
import wiringpi as wp
import time
import sys

servo_pin = 12

def set_deg(deg):
    move_deg = int( 81.0 + 41.0 / 90.0 * deg )
    return (move_deg)

def setup():
    wp.wiringPiSetupGpio()
    wp.pinMode( servo_pin, 2 )
    wp.pwmSetMode(0)
    wp.pwmSetRange(1024)
    wp.pwmSetClock(375)



param = sys.argv
deg = int(param[1])
print(deg)

setup()

if ( ( deg >= -90 ) and ( deg <= 90 ) ):
    move_deg = set_deg(deg)
    wp.pwmWrite( servo_pin, move_deg )

    time.sleep(0.5)

    wp.pwmWrite( servo_pin, 0 )
