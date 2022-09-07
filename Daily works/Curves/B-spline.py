import tkinter as tk
import numpy as np

global interval 
interval = 0.01

class Curve:
    knots = []
    points = []
    lines = []
    t_points = []
    b_spline = []
    t_b_spline = []
    t_b_spline_lines = []
    degree = None
    movingPoint = None
    interval = None
    
    def __init__(self):
        global interval
        self.knots = []
        self.points = []
        self.lines = []
        self.t_points = []
        self.b_spline = np.asarray([])
        self.t_b_spline = []
        self.t_b_spline_lines = []
        self.degree = 3
        self.movingPoint = None
        # Set the t's interval as this number
        self.interval = interval

    def N(self, k, j, t):
        if k==0:
            if self.knots[j]<= t and t<=self.knots[j+1]:
                return 1
            else:
                return 0
        else:
            return (t-self.knots[j])/(self.knots[j+k]-self.knots[j])*self.N(k-1, j, t) + (self.knots[j+k+1]-t)/(self.knots[j+k+1]-self.knots[j+1])*self.N(k-1, j+1, t)

    def draw_b_spline(self, canva):
        length = len(self.t_b_spline)
        for idx in range(0, length-1):
            canva.delete(self.t_b_spline[idx])
        if length > 0:
            canva.delete(self.t_b_spline[length-1])

        self.t_b_spline_lines = []
        self.t_b_spline = []
        self.b_spline = np.asarray([])

        n = len(self.points) - 1 
        k = self.degree
        m = n + k + 1
        for t in np.arange(self.knots[k], self.knots[n+1], self.interval):
            Sum = np.zeros(2)
            for j in range(0, n+1):
                Sum += np.asarray(self.points[j])*self.N(k, j, t)
            b_t = Sum
            self.b_spline = np.append(self.b_spline, b_t)
            t_b_t = canva.create_oval(b_t[0]-1, b_t[1]-1, b_t[0], b_t[1], fill="#000000")
            self.t_b_spline.append(t_b_t)

    # Moving a control point
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
        # each time moving a point, draw the b_spline curve again
        self.draw_b_spline(canva)
   
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
        # update knots
        self.knots = np.asarray(range(0, self.degree + idx + 1))
         
        #if idx > self.degree:
            #self.draw_b_spline(canva)
        self.draw_b_spline(canva)
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
    window.title('B-spline Curve')
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
