#!/usr/bin/python
import os.path
import serial
import sys
import subprocess

if __name__ == '__main__':

        if len(sys.argv) != 3:
                print "Usage: ", os.path.basename(sys.argv[0]), "<port> <address>"

        comport = sys.argv[1]
        addr = sys.argv[2]

        ser = serial.Serial()

        try:
                success=True
                ser = serial.Serial(sys.argv[1], 9600, timeout = 2.0)
                print("Setting up usb-gpib device")
                ser.write('++mode 1\n')
                ser.write('++addr ' + addr + '\n')
                ser.write('++auto 1\n')
                print("Setting up scope screen plot parameters")
                ser.write('HCSU port,gpib,dev,hp7470a,pens,4\n')
                print("Acquiring screen capture")
                ser.write('screen_dump\n')
                s = ser.read(65536)
                f = open("scope_output.txt","w")
                f.write(s)
                print("Done writing to file!  Use HP2xx to convert to image.")

                subprocess.call(["hp2xx","-c","12345","-f","conv_screencap.png","-m","png","scope_output.txt"])
                print("Finished converting image to png")
        except serial.SerialException, e:
                print e

        except serial.KeyboardInterrupt, e:
                print e
                ser.close()
