import pyautogui, sys, time
mx, my = pyautogui.position()

vx,vy=0,0

width,height = pyautogui.size()

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        y+=2
        vx,vy=x-mx,y-my
        mx=x
        my=y
        #vy-=0.3
        x+=vx*.9
        y+=vy*.9
        
        if x < 0:
            x+=width
            mx+=width
        if y < 0:
            y+=height
            my+=height
        if x > width:
            x-=width
            mx-=width
        if y > height:
            #y-=height
            #my-=height
            y-=vy*2
            vy=-vy
        
        pyautogui.moveTo(x, y, duration=.002)#, pyautogui.easeOutQuad)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        #print(positionStr)
        #print('\b' * len(positionStr))
        #sys.stdout.flush()
        #time.sleep(.2)
except KeyboardInterrupt:
    print('\n')
