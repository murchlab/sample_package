from gcode_tools import *

gcode_dir = r"../g-code/"

# mill_tool(gcode_dir + "xt332.txt")
drill_tool(gcode_dir + "xtc43.txt", Z=-0.015, pecking=False)
drill_tool(gcode_dir + "xtc32.txt", Z=-0.135, pecking=False)
drill_tool(gcode_dir + "xtc3mm.txt", Z=-0.135, pecking=False)
drill_tool(gcode_dir + "xt43.txt", Z=-0.620, pecking=True)
drill_tool(gcode_dir + "xt32.txt", Z=-0.620, pecking=True)
drill_tool(gcode_dir + "xt3mm.txt", Z=-0.620, pecking=True)
# mill_tool(gcode_dir + "xb332.txt")
# mill_tool(gcode_dir + "yt332.txt")
drill_tool(gcode_dir + "ytc45.txt", Z=-0.015, pecking=False)
drill_tool(gcode_dir + "ytc43.txt", Z=-0.55, pecking=False)
drill_tool(gcode_dir + "ytc2p3.txt", Z=-0.105, pecking=False)
drill_tool(gcode_dir + "ytc3mm.txt", Z=-0.55, pecking=False)
drill_tool(gcode_dir + "yt45.txt", Z=-0.0667, pecking=True)
drill_tool(gcode_dir + "yt43.txt", Z=-0.300, pecking=True)
drill_tool(gcode_dir + "yt2p3.txt", Z=-0.300, pecking=True)
drill_tool(gcode_dir + "yt3mm.txt", Z=-0.300, pecking=True)
# mill_tool(gcode_dir + "yb332.txt")

