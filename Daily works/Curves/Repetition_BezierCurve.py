import tkinter as tk
import numpy as np

global interval 
interval = 0.01

class Curve:
    points = []
    lines = []
    t_points = []
    bezier = []
    t_bezier = []
    t_beizer_lines = []
    movingPoint = None
    interval = None
    
    def __init__(self):
        global maxPointNum
        global interval
        self.points = []
        self.lines = []
        self.t_points = []
        self.bezier = np.asarray([])
        self.t_bezier = []
        self.t_bezier_lines = []
        self.movingPoint = None
        # Set the t's interval as this number
        self.interval = interval

    def bezier_add_line(self, canva):
        lineN = len(self.t_bezier) - 1
        for i in range(0, lineN):
            line = canva.create_line(self.bezier[i][0], self.bezier[i][1], self.bezier[i+1][0], self.bezier[i+1][1])
            self.t_bezier_lines.append(line)

    # This function is to use Bernstein Polynomial to compute Bezier Curve
    def draw_bezier(self, canva):
        length = len(self.t_bezier)
        for idx in range(0, length-1):
            canva.delete(self.t_bezier[idx])
            canva.delete(self.t_bezier_lines[idx])
        if length > 0:
            canva.delete(self.t_bezier[length-1])
        self.t_bezier_lines = []
        self.t_bezier = []
        self.bezier = np.asarray([])
        n = len(self.points) - 1
        np_points = np.asarray(self.points)
        for t in np.arange(0, 1+self.interval, self.interval):
            array = []
            for r in range(0, n+1):
                array.append([])
                for i in range(0, n-r+1):
                    if r==0:
                        array[r].append(np_points[i])
                    else:
                        array[r].append((1-t)*array[r-1][i] + t*array[r-1][i+1])
            b_t = array[n][0]
            self.bezier = np.append(self.bezier, b_t)
            t_b_t = canva.create_oval(b_t[0]-1, b_t[1]-1, b_t[0], b_t[1], fill="#000000")
            self.t_bezier.append(t_b_t)
        self.bezier = self.bezier.reshape(len(self.t_bezier), 2)
        self.bezier_add_line(canva)


    def move_point(self, x, y, canva):
        idx = self.movingPoint
        pre_line = None
        next_line = None

        canva.move(self.t_points[idx], x-self.points[idx][0], y-self.points[idx][1])
        self.points[idx] = (x, y)

        if idx > 0:
            pre_line = self.lines[idx-1]
            canva.delete(pre_line)
            self.lines[idx-1] = canva.create_line(self.points[idx-1][0], self.points[idx-1][1],self.points[idx][0], self.points[idx][1])

        if idx < len(self.points)-1:
            next_line = self.lines[idx]
            canva.delete(next_line)
            self.lines[idx] = canva.create_line(self.points[idx][0], self.points[idx][1], self.points[idx+1][0], self.points[idx+1][1])
        self.draw_bezier(canva)
   
    def move_or_add(self, x, y, canva):
        is_move = False
        idx = 0
        for idx in range(0, len(self.points)):
            p = self.points[idx]
            if p[0]-5<=x and x<=p[0]+5 and p[1]-5<=y and y<=p[1]+5:
                is_move = True
                break
        if is_move:
            # move this point
            self.movingPoint = idx
            self.move_point(x, y, canva)
        else:
            # add this point as a control point
            self.add_point(x, y, canva)

    def add_point(self, x, y, canva):
        # add a new point, first draw this point 
        point = canva.create_oval(x-4, y-4, x+4, y+4, fill="#000000")
        # add this new point as a control point
        self.points.append((x, y))
        self.t_points.append(point)
        idx = len(self.points)
        # If there are 3 or more points, we can draw Bezier curve
        if idx > 2:
            self.draw_bezier(canva)
        # if there are 2 or more points, we can draw lines between points
        if idx >= 2:
            idx -= 1
            line = canva.create_line(self.points[idx-1][0], self.points[idx-1][1], self.points[idx][0], self.points[idx][1])
            self.lines.append(line)

global curve
curve = Curve()

def click(event, canva):
    global curve
    x = event.x
    y = event.y
    if curve.movingPoint is None:
        # Add a new point 
        curve.move_or_add(x, y, canva)

def moving(event, canva):
    global curve
    if curve.movingPoint is None:
        pass
    else:
        curve.move_point(event.x, event.y, canva)
    
def stop_move(event, canva):
    curve.movingPoint = None

def main():
    # some initial setting
    window = tk.Tk()
    window.title('Bezier Curve')
    window.geometry('800x800')
    canva = tk.Canvas(window, width=800, height=800)
    
    # A mouse button is pressed.
    window.bind('<Button-1>', lambda event: click(event, canva=canva))
    # The mouse is moved, with mouse button 1 being held down. 
    window.bind('<B1-Motion>', lambda event: moving(event, canva=canva))
    # Button 1 was released.
    window.bind('<ButtonRelease-1>', lambda event: stop_move(event, canva=canva))

    canva.pack()

    window.mainloop()
    

if __name__ == '__main__':
    main()
