from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform




"""
def GameObject(object):
    def __init__(self):
        self.pos = vec2d(0,0)

    def __update__(self):
        pass

def DrawableObject(GameObject):
    def __draw__(self,screen):
        pass

def aStar(self, world, graph, current, end):
    open_list = set()
    closed_list = set()
    path = []

    def retracePath(c):
        path.insert(0,c)
        if c.parent == None:
            return
        retracePath(c.parent)

    open_list.append(current)
    while len(open_list) is not 0:
        current = min(open_list, key=lambda inst:inst.H)
        

class Box(object):
    def __init__(self,rect):
        self.rect = rect

class Unit(object):
    def __init__(self, world):
        self.world = world
        self.pos = vec2d(0,0)
        self.waypoints = []
        self.waypoints.append(vec2d(uniform(0,640),uniform(0,480)))
        self.current_waypoint = self.waypoints[0]

        self.sneak_speed = 1
        self.walk_speed = 2
        self.run_speed = 3

        self.move_speed = self.walk_speed

    def add_waypoint(self,pos):

        self.waypoints.append(vec2d(pos))

    def remove_waypoint(self,wp=None):
        if wp is None:
            self.waypoints.pop()
        elif wp in self.waypoints:
            self.waypoints.remove(wp)

    def update(self):
        # Check for missing waypoints
        if self.current_waypoint not in self.waypoints:
            self.current_waypoint = self.pos
        dir = self.current_waypoint - self.pos
        if dir.length > self.move_speed:
            dir.length = self.move_speed
            self.pos += dir
        else:
            self.pos = self.current_waypoint
            try:
                self.waypoints.remove(self.current_waypoint)
            except ValueError:
                pass
            if len(self.waypoints) > 0:
                self.current_waypoint = self.waypoints[0]
            else:
                self.waypoints.append(self.pos)
                self.current_waypoint = self.waypoints[0]

"""

BLACK = (0,0,0)
LIGHTGRAY = (211,211,211)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Starter(PygameHelper):
    def __init__(self):
       
        self.w, self.h = 1200, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        
        
        """
        self.select_toggle = False
        self.selected = []

        self.units = []
        self.enemy = []
        self.static_objects = []

        # Add a test unit
        u = Unit(self)
        u.pos = vec2d(uniform(0,640),uniform(0,480))
        self.units.append(u)

        # Add a wall

        """
    def update(self):
        pass
        """
        for u in self.units:
            u.update()

        for u in self.units:
            for u2 in self.units:
                if u == u2: continue
                d = u.pos.get_distance(u2.pos)
                if d < 40:
                    # Reslove Collisions
                    overlap = 40 - d
                    dir = u2.pos - u.pos
                    dir.length = overlap/2
                    u2.pos += dir
                    u.pos -= dir
        """
    def keyDown(self, key):
        pass
        """
        if key == 304:
            self.select_toggle = True
        # Backspace Removes Last Waypoint
        elif key == 8:
            for u in self.selected:
                u.remove_waypoint()
        """
    def keyUp(self, key):
        pass
        """
        print ("Debug: Key Pressed(%i)" % key)
        if key == 49:
            for u in self.selected:
                u.move_speed = u.sneak_speed
        elif key == 50:
            for u in self.selected:
                u.move_speed = u.walk_speed
        elif key == 51:
            for u in self.selected:
                u.move_speed = u.run_speed
        if key == 304:
            self.select_toggle = False
        """
    def mouseUp(self, button, pos):
        pass
        """
        if button == 3:
            for u in self.selected:
                u.add_waypoint(pos)
        elif button == 1:
            for u in self.units:
                if u.pos.get_distance(vec2d(pos)) <= 20:
                    if self.select_toggle:
                        self.selected.append(u)
                    else:
                        self.selected = [u]
            
        """
    def mouseMotion(self, buttons, pos, rel):
        if 100 <= pos[0] <= 500 and 100 <= pos[1]<= 500:
                x = pos[0] - 100
                y = 500 - pos[1]
                theta_1 = (x/400)*2*pi
                theta_2 = (y/400)*2*pi
                
                #draw the base
                self.screen.fill((255,255,255))
                pygame.draw.line(self.screen, LIGHTGRAY, [100,400],[300, 500],2)
                pygame.draw.line(self.screen, LIGHTGRAY, [100,300],[200, 500],2)
                pygame.draw.line(self.screen, LIGHTGRAY, [400,100],[500,300],2)
                pygame.draw.line(self.screen, LIGHTGRAY, [300,100],[500,200],2)
                pygame.draw.rect(self.screen, BLACK, (100,100, 400,400),2 )
                pygame.draw.line(self.screen, BLACK, [100,400],[167,433], 2)
                pygame.draw.line(self.screen, BLACK, [167,433],[200,500],2)
                pygame.draw.line(self.screen, BLACK, [400,100],[433, 167],2)
                pygame.draw.line(self.screen, BLACK, [433,167],[500,200],2)
                
                strc1_w = 900 + 200*cos(pi/6)
                strc1_h = 400 - 200*sin(pi/6)
                strc2_w = 700 + 200*cos(pi/6)
                strc2_h = 400 - 200*sin(pi/6)
                baseList = [[700,400],[900,400],[strc1_w,strc1_h], [strc2_w,strc2_h]]
                pygame.draw.polygon(self.screen, GREEN, baseList,2)
                
                p21_w = 900 - 200 * cos(theta_2)
                p21_h = 400 - 200 * sin(theta_2)
                p22_w = p21_w + 200 * cos(pi/6)
                p22_h = p21_h - 200 * sin(pi/6)
                plane2List = [[900,400],[p21_w,p21_h],[p22_w,p22_h],[strc1_w,strc1_h]]
                pygame.draw.polygon(self.screen, RED, plane2List,2)
                
                p11_w = 700 + 200 * cos(theta_1)
                p11_h = 400 - 200 * sin(theta_1)
                p12_w = p11_w + 200 * cos(pi/6)
                p12_h = p11_h - 200 * sin(pi/6)
                plane1List = [[700, 400],[p11_w,p11_h],[p12_w, p12_h],[strc2_w, strc2_h]]
                pygame.draw.polygon(self.screen, BLUE, plane1List,2)
     
        else:
            self.screen.fill((255,255,255))
            pygame.draw.line(self.screen, LIGHTGRAY, [100,400],[300, 500],2)
            pygame.draw.line(self.screen, LIGHTGRAY, [100,300],[200, 500],2)
            pygame.draw.line(self.screen, LIGHTGRAY, [400,100],[500,300],2)
            pygame.draw.line(self.screen, LIGHTGRAY, [300,100],[500,200],2)
            pygame.draw.rect(self.screen, BLACK, (100,100, 400,400),2 )
            pygame.draw.line(self.screen, BLACK, [100,400],[167,433], 2)
            pygame.draw.line(self.screen, BLACK, [167,433],[200,500],2)
            pygame.draw.line(self.screen, BLACK, [400,100],[433, 167],2)
            pygame.draw.line(self.screen, BLACK, [433,167],[500,200],2)
                
        
    def draw(self):
        pass
    
        """
        for u in self.units:
            # Draw Unit Waypoints
            line_start = u.pos
            for wp in u.waypoints:
                if wp == u.current_waypoint:
                    pygame.draw.circle(self.screen,(0,0,255),wp.inttup(), 30, 1)
                    pygame.draw.line(self.screen,(0,0,255),line_start.inttup(),wp.inttup())
                else:
                    pygame.draw.circle(self.screen,(255,0,0), wp.inttup(), 30, 1)
                    pygame.draw.line(self.screen,(255,0,0),line_start.inttup(),wp.inttup())
                line_start = wp
                
            # Draw Unit
            pygame.draw.circle(self.screen,(0,0,0), u.pos.inttup(), 21)
            if u in self.selected:
                pygame.draw.circle(self.screen,(100,255,100), u.pos.inttup(), 20)
            else:
                pygame.draw.circle(self.screen,(200,200,255), u.pos.inttup(), 20)
        """
    
        
s = Starter()
s.mainLoop(40)


