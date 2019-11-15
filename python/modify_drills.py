from gcode_tools import *

gcode_dir = r"../g-code/"

drill_tool(gcode_dir + "ttc.txt", Z=-0.015, pecking=True)
drill_tool(gcode_dir + "tt43.txt", Z=-0.620, pecking=True)
drill_tool(gcode_dir + "tt32.txt", Z=-0.620, pecking=True)
drill_tool(gcode_dir + "tt3mm.txt", Z=-0.620, pecking=True)
drill_tool(gcode_dir + "btc.txt", Z=-0.015, pecking=True)
drill_tool(gcode_dir + "bt45.txt", Z=-0.0667, pecking=True)
drill_tool(gcode_dir + "bt43.txt", Z=-0.300, pecking=True)
drill_tool(gcode_dir + "bt3mm.txt", Z=-0.300, pecking=True)

