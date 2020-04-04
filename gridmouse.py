import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller
import threading
import ctypes

pyautogui.FAILSAFE = False

class GridMouse:
        IS_PAUSED = False
        def __init__(self):
                self.grid = self.grid_generation(3)
                self.combos = {self.toggle_state:['alt_l','x'],exit:['alt_l','c']}
                self.gl = ["1","2","3","4","5","6","7","8","9"]
                self.lclick = "q"
                self.rclick = "w"
                self.dclick = "e"

        def init(self):
                print("Started")
                self.start_keyboard_listener(True)

        pressed_keys = []

        def match_lists(self,l1,l2):
                        if l1 != l2:
                                return False
                        return True

        def toggle_state(self):
                if self.IS_PAUSED == True:
                        print("<Switched to MouseControl mode>")
                        self.IS_PAUSED = False
                        self.listener.stop()

                        self.listener = keyboard.Listener(on_press = self.on_press,on_release = self.on_release,suppress=True)
                        self.listener.start()
                        self.listener.join()
                else:
                        print("<Switched to NormalControl mode>")
                        self.IS_PAUSED = True
                        self.listener.stop()

                        self.listener = keyboard.Listener(on_press = self.on_press,on_release = self.on_release,suppress=False)
                        self.listener.start()
                        self.listener.join()


        def on_press(self,key):
                k = None
                if key == keyboard.Key.esc:
                        exit()
                try:
                        k = key.char
                except Exception as e:
                        k = key.name

                self.pressed_keys.append(k)
                for c in self.combos:
                        if self.match_lists(self.combos[c],self.pressed_keys) == True:
                                c()
                        
                if self.IS_PAUSED == False:
                        if k in self.gl:
                                raw = []
                                for r in self.grid:
                                        for c in r:
                                                raw.append(c)
                                bounds = raw[self.gl.index(k)]
                                print("Move to quadrant "+<str(self.gl.index(k)+1))
                                get_middle = (((bounds[0][0]+bounds[1][0])//2),((bounds[0][1]+bounds[2][1])//2))
                                pyautogui.moveTo(get_middle[0],get_middle[1])
                        if k in ['left','right','up','down']:
                                step = 15
                                mpos = Controller().position
                                if k == 'left':
                                        pyautogui.moveTo(mpos[0]-step,mpos[1])
                                elif k == 'right':
                                        pyautogui.moveTo(mpos[0]+step,mpos[1])
                                elif k == 'up':
                                        pyautogui.moveTo(mpos[0],mpos[1]-step)
                                elif k == 'down':
                                        pyautogui.moveTo(mpos[0],mpos[1]+step)
                        if k in [self.lclick,self.rclick,self.dclick]:
                                        if k == self.lclick:
                                                Controller().press(Button.left)
                                                Controller().release(Button.left)
                                        if k == self.rclick:
                                                Controller().press(Button.right)
                                                Controller().release(Button.right)
                                        if k == self.dclick:
                                                Controller().click(Button.left,2)

                                                
        def on_release(self,key):
                self.pressed_keys = []

        def start_keyboard_listener(self,suppressed):
                self.listener = keyboard.Listener(on_press = self.on_press,on_release = self.on_release,suppress=suppressed)
                self.listener.start()
                self.listener.join()

        def grid_generation(self,cut_point):
                ''' return matrix mxn representing grid, where each x in mxn represents box bounds as (x,y) set 0:topleft 1:topright 2:bottomleft 3 bottomrigth'''
                winsize = pyautogui.size()
                x,y = winsize[0],winsize[1]

                grid_repr = []

                ox,oy = x//cut_point,y//cut_point


                tx,ty = 0,0

                for i in range(0,3):
                        tx += ox
                        ty += oy
                        grid_repr.append([(tx,ty)])

                pg = (0,0)

                for g in grid_repr:
                        q4 = g[0]
                        if grid_repr.index(g) == 0:
                                q1 = (0,0)
                                q2 = (q4[0],0)
                                q3 = (0,q4[1])
                        else:
                                prev = pg
                                q1 = (prev[0],prev[1])
                                q2 = (q4[0],prev[1])
                                q3 = (prev[0],q4[1])
                        pg = q4
                        grid_repr[grid_repr.index(g)] = [q1,q2,q3,q4]

                grid_matrix = [[g] for g in grid_repr]

                tgm = []

                for r in grid_matrix:
                        col = [0,0,0]
                        set = grid_matrix.index(r)
                        col[set] = r[0]
                        if col[-1] != 0:
                                tcol = col[::-1]
                                for c in tcol:
                                        if c == 0:
                                                prev = tcol[tcol.index(c)-1]
                                                pq1,pq2,pq3,pq4 = prev[0],prev[1],prev[2],prev[3]
                                                q1 = (pq1[0]-ox,pq1[1])
                                                q2 = pq1
                                                q3 = (pq3[0]-ox,pq3[1])
                                                q4 = pq3
                                                tcol[tcol.index(c)] = [q1,q2,q3,q4]
                                col = tcol[::-1]
                        elif col[0] != 0:
                                for c in col:
                                        if c == 0:
                                                prev = col[col.index(c)-1]
                                                pq1,pq2,pq3,pq4 = prev[0],prev[1],prev[2],prev[3]
                                                q1 = pq2
                                                q2 = (q1[0]+ox,q1[1])
                                                q3 = pq4
                                                q4 = (q3[0]+ox,q3[1])
                                                col[col.index(c)] = [q1,q2,q3,q4]
                        else:
                                for i in range(set+1,len(col)):
                                        c = col[i]
                                        if c == 0:
                                                prev = col[i-1]
                                                pq1,pq2,pq3,pq4 = prev[0],prev[1],prev[2],prev[3]
                                                q1 = pq2
                                                q2 = (q1[0]+ox,q1[1])
                                                q3 = pq4
                                                q4 = (q3[0]+ox,q3[1])
                                                col[i] = [q1,q2,q3,q4]
                                tcol = col[::-1]
                                for c in tcol:
                                        if c == 0:
                                                prev = tcol[tcol.index(c)-1]
                                                pq1,pq2,pq3,pq4 = prev[0],prev[1],prev[2],prev[3]
                                                q1 = (pq1[0]-ox,pq1[1])
                                                q2 = pq1
                                                q3 = (pq3[0]-ox,pq3[1])
                                                q4 = pq3
                                                tcol[tcol.index(c)] = [q1,q2,q3,q4]
                                col = tcol[::-1]

                        tgm.append(col)

                grid_matrix = tgm

                return grid_matrix;








GridMouse().init()
