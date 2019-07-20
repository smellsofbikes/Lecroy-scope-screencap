# Lecroy-scope-screencap
Takes screen captures for LeCroy 94xx series scopes using Prologix usb-gpib converter, uses HP2xx
This is not fancy or flexible: all it takes for arguments are the /dev/ttyUSB port and the gpib address of the scope.
It sets up the scope to screen dump as a Hewlett Packard 7470A plotter, then uses HP2xx to convert the HPGL to a png.
