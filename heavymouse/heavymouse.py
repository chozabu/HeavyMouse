import sys, time, math
from pymouse import PyMouse

try:
    import defopt
except ImportError:
    print("could not import defopt, command line options will not work")
    print("try 'pip install defopt'")

'''

              ___
     _  _  .-'   '-.
    (.)(.)/         \   jgs (art from http://www.ascii-code.com/ascii-art/animals/rodents/mice.php)
     /@@             ;
    o_\\-mm-......-mm`~~~~~~~~~~~~~~~~`    
'''

def main(drag=0.02, grav=1.5, bottom='bounce', left='bounce', right='bounce', top='bounce', allsides=None, maxspeed=40, framerate=50):
    """HeavyMouse - a python mouse mover\n  
    
    example, for bouncy walls, no gravity and less speed:  \n
    python heavymouse.py --drag .04 --grav 0 --allsides bounce --maxspeed 10

    :param float drag: amount of drag. 0.0 to 1.0, default is 0.02
    :param float grav: gravity, default is 1.5
    :param str bottom: can be 'bounce', 'wrap' or 'stop' - default is bounce
    :param str left: can be 'bounce', 'wrap' or 'stop' - default is bounce
    :param str right: can be 'bounce', 'wrap' or 'stop' - default is bounce
    :param str top: can be 'bounce', 'wrap' or 'stop' - default is bounce
    :param str allsides: will override settings for each side - no default
    :param int maxspeed: prevent the mouse moving (much) faster than this each frame - default is 40
    :param int framerate: frequency the program operates at - default is 50

    """
    friction = 1.0-drag
    
    sleeptime = 1000.0/framerate/1000.0

    if allsides:
        top=right=left=bottom=allsides
    print(top, bottom)


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
            vx*=friction
            vy*=friction
            
            #gravity
            vy+=grav
            
            vel = (math.sqrt(vx**2+vy**2))
            if vel > maxspeed:
                vx*=.7
                vy*=.7
            
            #update current and previous position
            mx=x
            my=y
            x+=vx
            y+=vy
            
            #wrap or bounce at screen edges
            if x < 0:
                if left == 'wrap':
                    x+=width
                    mx+=width
                elif left == 'bounce':
                    x-=vx*2
                    xy=-vx
                else: #stop
                    x=0
            
            if y < 0:
                if top == 'wrap':
                    y+=height
                    my+=height
                elif top == 'bounce':
                    y-=vy*2
                    vy=-vy
                else: #stop
                    y=0
            
            if x > width:
                if right == 'wrap':
                    x-=width
                    mx-=width
                elif right == 'bounce':
                    x-=vx*2
                    xy=-vx
                else: #stop
                    x=width
            
            if y > height:
                if bottom == 'wrap':
                    y-=height
                    my-=height
                elif bottom == 'bounce':
                    y-=vy*2
                    vy=-vy
                else: #stop
                    y=height
            
            #apply position to mouse
            m.move(int(x), int(y))
            
            #debug output
            #positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            #print(positionStr)
            #print(vx, vy)
            #print('\b' * len(positionStr))
            #sys.stdout.flush()
            
            time.sleep(sleeptime)
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':
    try:
        defopt.run(main)
    except NameError:
        main()