import tkinter as tk
import numpy as np

global interval 
interval = 0.01

class Curve:
    knots = []
    points = []
    lines = []
    t_points = []
    lag = []
    t_lag = []
    movingPoint = None
    interval = None
    
    def __init__(self):
        global interval
        self.knots = []
        self.points = []
        self.t_points = []
        self.lag = np.asarray([])
        self.t_lag = []
        self.movingPoint = None
        # Set the t's interval as this number
        self.interval = interval

    def L(self, n, i, t):
        up = 1
        down = 1
        for j in range(0, n+1):
            if j==i:
                pass
            else:
                up *= (t-self.knots[j])
                down *= (self.knots[i] - self.knots[j])
        return up/down

    def draw_lag(self, canva):
        length = len(self.t_lag)
        for idx in range(0, length-1):
            canva.delete(self.t_lag[idx])
        if length > 0:
            canva.delete(self.t_lag[length-1])

        self.t_lag = []
        self.lag = np.asarray([])
        n = len(self.knots) - 1
        for t in np.arange(self.knots[0], self.knots[n], self.interval):
            Sum = np.zeros(2)
            for i in range(0, n+1):
                Sum += np.asarray(self.points[i])*self.L(n, i, t)
            b_t = Sum
            self.lag = np.append(self.lag, b_t)
            t_b_t = canva.create_oval(b_t[0]-1, b_t[1]-1, b_t[0], b_t[1], fill="#000000")
            self.t_lag.append(t_b_t)

    # Moving a control point
    def move_point(self, x, y, canva):
        idx = self.movingPoint

        canva.move(self.t_points[idx], x-self.points[idx][0], y-self.points[idx][1])
        self.points[idx] = (x, y)

        # each time moving a point, draw the curve again
        self.draw_lag(canva)
   
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
        self.knots = np.asarray(range(0, idx))
         
        self.draw_lag(canva)

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
