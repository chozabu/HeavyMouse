#HeavyMouse

This is a silly program, designed to give your mouse momemtum, gravity and wrap/bounce at the screens edge.

###Deps:

    sudo apt-get install python3-xlib
    #OR
    sudo apt-get install python-xlib
    
    
    pip install pyuserinput
    
    #optional, for CLI options to control drag and gravity
    pip install defopt


##Running:

    python heavymouse.py

grav and drag are supported as args, so you can try:

    python heavymouse.py --grav 1.5 --drag 0.02 #default settings
    python heavymouse.py --grav 0 --drag 0.2 #more usable

    

###Alternate version

using pyautogui instead of pymouse/pyinput:

    sudo apt-get install python3-tk
    sudo apt-get install python3-xlib
    pip3 install pyautogui
    
    python3 alternate_heavymouse.py
    
Sorry about the low update-rate (jerkyness) on pyautogui version - a PR to fix it would be very welcome ;)

##Development

This is a tiny toy app developed for my own enjoyment - and hopefully yours too.  
There are loads of tweaks that could be done if you fancy writing a little code

 - options for effect at screen edges (bounce/wrap/other)
 - options to control other features
 - auto-detect mouse control backend?
 - package for pypi or debian?
 - improve momentum implementation (strangeness, due to mouse position being an int)
 - visual effects? like a trail following the mouse (this may be hard to do cross platform, but even single platform is fine if it fails gracefully) 
