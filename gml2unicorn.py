#!/usr/bin/env python

#########
# USAGE #
#########
#
# 1. Edit the configuration section below to match your Unicorn setup.
# 2. Acquire a GML file (http://000000book.com/)
# 3. python gml2unicorn.py my_graffiti.gml > my_graffiti.gcode
# 4. Load my_graffiti.gcode into ReplicatorG
# 5. Build!

### BEGIN CONFIGURATION ###
feedrate = 3500
start_delay = 150
stop_delay = 150
pen_up_angle = 50
pen_down_angle = 30
# Standard PostIt note pads are 75mm x 75mm
page_width = 74
page_height = 74
### END CONFIGURATION ###

import sys
# https://bitbucket.org/keegan3d/pygml
import PyGML

pen_up = [
          "M300 S%d (pen up)" % pen_up_angle,
          "G4 P%d (wait %dms)" % (stop_delay, stop_delay)
         ]

pen_down = [
          "M300 S%d (pen down)" % pen_down_angle,
          "G4 P%d (wait %dms)" % (start_delay, start_delay)
         ]

preamble = [
            "G21 (metric ftw)", 
            "G90 (absolute mode)",
            "G92 X0 Y0 Z0 (zero all axes)"
           ]
preamble.extend(pen_up)

postscript = ["(End of print job)"]
postscript.extend(pen_up)
postscript.extend([
                  "G1 X0 Y0 F%d (retrieving platform)" % (feedrate),
                  "M18 (disengage drives)"
                  ])

def client_info(client):
  headers = []
  for hdr in ["username", "name", "uniqueKey", "version", "keywords"]:
    headers.append("(%s: '%s')" % (hdr, client.get(hdr)))
  return headers

def move_to(x,y):
  my_x = (x * -page_width) - page_width/2
  my_y = (y * page_height) - page_height/2
  return "G1 X%0.2F Y%0.2F F%0.2F" % (my_x, my_y, feedrate)

def readFile(filename):
    gmlFile = open(filename, 'r')
    gml = PyGML.GML(gmlFile)
    gmlFile.close()
    return gml


if __name__ == '__main__':
    gml = readFile(sys.argv[1])
   
    for line in client_info(gml.client()):
      print line

    for line in preamble:
      print line

    for stroke in gml.iterStrokes():
        first_point = True
        for point in stroke.iterPoints():
            print move_to(point.x, point.y)
            if (first_point):
              for line in pen_down:
                print line
              first_point = False
        for line in pen_up:
          print line

    for line in postscript:
      print line

