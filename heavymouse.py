import sys, time
from pymouse import PyMouse

m = PyMouse()

mx, my = m.position()
mx,my=float(mx), float(my)

vx,vy=.0,.0

width,height = m.screen_size()

print('Press Ctrl-C to quit.')
try:
    while True:
        #get current position
        x, y = m.position()
        x,y=float(x), float(y)
        
        #alter vel by user input
        vx += float(x-mx)-vx+.5
        vy += float(y-my)-vy+.5
        
        #drag
        vx*=0.98
        vy*=0.98
        
        #gravity
        vy+=1.5
        
        #update current and previous position
        mx=x
        my=y
        x+=vx
        y+=vy
        
        #wrap or bounce at screen edges
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
        
        #apply position to mouse
        m.move(x, y)
        
        #debug output
        #positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        #print(positionStr)
        #print(vx, vy)
        #print('\b' * len(positionStr))
        #sys.stdout.flush()
        
        #100 FPS maximum?
        time.sleep(.02)
except KeyboardInterrupt:
    print('\n')
