#HeavyMouse

This is a silly program, designed to give your mouse momemtum, gravity and wrap/bounce at the screens edge.

Deps:

    sudo apt-get install python3-xlib
    #OR
    sudo apt-get install python-xlib
    
    
    pip install pyuserinput
    
    #optional, for CLI options to control drag and gravity
    pip install defopt


To run:

    python heavymouse.py

Alternate version, using pyautogui instead of pymouse/pyinput:

    sudo apt-get install python3-tk
    sudo apt-get install python3-xlib
    pip3 install pyautogui
    
    python3 alternate_heavymouse.py
    
Sorry about the low update-rate (jerkyness) on pyautogui version - a PR to fix it would be very welcome ;)
