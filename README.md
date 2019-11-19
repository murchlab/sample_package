# Sample Package v1.2

## Purchase list

1. Copper rod stock

    Superconducting 101 copper rod, Diameter = 1.5"

    https://www.mcmaster.com/8965k75

2. Screws for fastening (4 for each)

    #4-40 Brass socket head screw, Length = 5/8"

    https://www.mcmaster.com/93465a111

3. Screws for mounting (2 for each)

    #4-40 Brass socket head screw, Length = 1"

    https://www.mcmaster.com/93465a114

4. Nuts for mounting (2 for each)

    #4-40 Brass hex nut, Width = 1/4", Height = 3/32"

    https://www.mcmaster.com/92671a005

5. Screws for thermalization (1 for each)

    #4-40 Brass socket head screw, Length = 1/4"

    https://www.mcmaster.com/93465a106
    
## Milling procedures

These g-code files are generated in a certain order. Particularly, I assume that the milling procedures are performed before the drilling ones.

#### The way I name the files:

1. The first letter:

        x: Stands for the top part
        y: Stands for the bottom part
        
2. The second letter:

        t: Stands for the topside of the part
        b: Stands for the bottomside of the part
        
3. Letter "c" indicates that this file is for center drills

4. The numbers indicats the tool to use.

### Top, Topside

1. Pockets: 3/32" End Mill

        xt332.txt

2. Center Drills

        xtc43.txt (Z = -0.015")
        xtc32.txt (Z = -0.135")
        xtc3mm.txt (Z = -0.135")
        
3. #4-40 tapped holes: #43 Drill Bit

        xt43.txt (Z = -0.620")

4. #4-40 close fit: #32 Drill Bit (Z = 0.620")

        xt32.txt (Z = -0.620")

5. #4-40 mounting holes: 3mm Drill Bit (Z = 0.620")

        xt3mm.txt (Z = -0.620")
          
### Top, Bottomside

1. The pocket: 3/32" End Mill

        xb332.txt
        
### Bottom, Topside

1. Pockets: 3/32" End Mill

        yt332.txt

1. Center Drills

        ytc45.txt (Z = -0.015")
        ytc43a.txt (Z = -0.105")
        ytc43b.txt (Z = -0.055")
        ytc3mm.txt (Z = -0.055")

2. Post pockets: #45 Drill Bit

        yt45.txt (Z = -0.0667")
        
3. #4-40 tapped holes and IO holes: #43 Drill Bit

        yt43.txt
        
4. #4-40 mounting holes: 3mm Drill Bit

        yt3mm.txt (Z = -0.300")
        

        
### Bottom, Bottomside

1. Pockets: 3/32" End Mill

        yb332.txt

## Guidelines for CNC machining (Bridgeport EZTrak)

### Workflow
    
1. Design the part using SolidWorks.

2. Generate the toolpaths using the built-in SolidWorks CAM.

3. Generate the g-code files using a post processor named "EZTRAK_G.ctl". One g-code file corresponding to one toolpath only (without tool change operations).

### Compatibility

The machine is old, which means certain commands are not recognized by this machine. The known examples include:
  
1. Drilling commands like G81, G83

2. Tool radius compensation commands like G40, G41

In order to bypass these commands, do not using the default "Contour Mill" and "Drill" operations in SolidWorksCAM.

### Milling

We do both roughing & finishing procedures. But the finishing procedure is manually defined as a special roughing procedure in SolidWorks Cam, in order to avoid the usage of "Contour Mill".

1. Spindle

        Spindle Speed = 2400 rpm

2. Feedrates:

        XY Feedrate = 8 in/min
    
        Z Feedrate = 4 in/min
        
        Leadin Feedrate = 4 in/min
    
3. Side parameters:

    a. For roughing
    
        Allowance = 0.01 in
        
        Stepover = 80%
      
    b. For finishing
    
          Allowance = 0 in
        
          Stepover = 80%
      
4. Depth parameters:

        Bottom Allowance = 0 in
    
        Island Allowance = 0 in
    
        First Cut Amount = 0.02 in
    
        Max Cut Amount = 0.02 in
    
        Final Cut Amount = 0.01 in
        
5. Rest machining:

    a. For roughing
    
        Machine: No
        
    b. For finishing
    
        Maching: From WIP (Work in Progress)
        
### Drilling

We do centering before drilling. G-code file for both procedures are currently created manualy. Spindle and feedrate parameters are the same as used in the milling procedures.

1. Center Drill

        Center Drill Depth = 0.015 in

2. Drill

        Add tip length: True

## Features to modify (Done)

1. Making the coaxial holes larger

    Reason: We want a coaxial cable covered with solder to pass through.

2. Making the inner diameter larger

    Reason: To make more space for the coax-to-cpw transition structure

3. Adding a "V" shaped groove for indium seal
3. Adding a place for solonoid
4. Think about a good way to mount the sample box
5. Adding holes for thermalization
6. Adding a light-tight but not air-tight structure

## Related projects

1. A new sample rack and a new copper bucket for our new fridge
