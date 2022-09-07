import tkinter as tk
import numpy as np

class Curve:
    points = []
    t_points = []
    lines = []
    Bspline_points = []
    t_Bspline_points = []
    movingPoint = None

    def __init__(self):
        global interval
        self.points = []
        self.t_points = []
        self.t_lines = []
        self.Bspline_points = []
        self.t_Bspliine_points = []
        self.movingPoint = None

    def move_or_add(self, x, y, canva):
        is_move = False
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
            # add this points as a control point
            self.add_point(x, y, canva)

    def add_point(self, x, y, canva):
        # add a new point, draw this point
        point = canva.create_oval(x-4, y-4, x+4, y+4, fill="#000000")
        self.t_points.append(point)
        # add this new point as control point
        self.points.append((x, y))
        if len(self.points) >= 3:
            self.delete_lines(canva)
            self.draw_lines_between_points(canva)

    def delete_lines(self, canva):
        for i in self.t_lines:
            canva.delete(i)

    def draw_lines_between_points(self, canva):
        num_lines = len(self.points)
        for i in range(0, num_lines-1):
            line = canva.create_line(self.points[i][0], self.points[i][1], self.points[i+1][0], self.points[i+1][1])
            self.t_lines.append(line)
        line = canva.create_line(self.points[num_lines-1][0], self.points[num_lines-1][1], self.points[0][0], self.points[0][1])
        line = self.t_lines.append(line)

    def delete_points(self, canva):
        for i in self.t_points:
            canva.delete(i)

    def draw_Bspline(self, canva):
        global degree
        #self.delete_points(canva)
        new_points = []
        new_t_points = []
        num_points = len(self.points)
        for i in range(0, num_points):
            point = self.points[i]
            x, y = point[0], point[1]
            new_points.append(point)
            t_point = canva.create_oval(x-4, y-4, x+4, y+4, fill="#000000")
            new_t_points.append(t_point)
            x = -1/16*self.points[(i-1+num_points)%num_points][0] + 9/16*self.points[i][0] + 9/16*self.points[(i+1)%num_points][0] - 1/16*self.points[(i+2)%num_points][0]
            y = -1/16*self.points[(i-1+num_points)%num_points][1] + 9/16*self.points[i][1] + 9/16*self.points[(i+1)%num_points][1] - 1/16*self.points[(i+2)%num_points][1]
            point = (x, y)
            new_points.append(point)
            t_point = canva.create_oval(x-4, y-4, x+4, y+4, fill="#000000")
        self.points = new_points
        self.t_points = new_t_points

global curve
curve = Curve()

def click(event, canva):
    global curve
    x = event.x
    y = event.y
    if curve.movingPoint is None:
        curve.move_or_add(x, y, canva)

def moving(event, canva):
    global curve
    if curve.movingPoint is None:
        pass
    else:
        curve.move_point(event.x, event.y, canva)

def stop_move(event, canva):
    curve.movingPoint = None

def draw_Bspline(event, canva):
    global curve
    if len(curve.points) < 3:
        print("At least 3 points\n")
    else:
        curve.delete_lines(canva)
        curve.draw_Bspline(canva)
        curve.draw_lines_between_points(canva)

def main():
    # some initial setting
    window = tk.Tk()
    window.title('B-Spline')
    window.geometry('800x800')
    canva = tk.Canvas(window, width=800, height=800)

    # A mouse button is pressed.
    window.bind('<Button-1>', lambda event: click(event, canva=canva))
    # The mouse is movin with mouse button 1 being held down.
    window.bind('<B1-Motion>', lambda event: moving(event, canva=canva))
    # Button 1 was released
    window.bind('<ButtonRelease-1>', lambda event: stop_move(event, canva=canva))
    # Button 'z' is pressed
    window.bind('z', lambda event: draw_Bspline(event, canva=canva))
    canva.pack()
    window.mainloop()

if __name__ == '__main__':
    main()
