import tkinter as tk
import numpy as np

global interval 
interval = 0.005
global degree

class Curve:
    interval = None
    
    def __init__(self):
        global interval
        # Set the t's interval as this number
        self.interval = interval

    # This function is to use Bernstein Polynomial to compute Bezier Curve
    def draw_bezier(self, canva):
        global degree
        n = degree
        B = []
        for t in np.arange(0, 1+self.interval, self.interval):
            B = []
            for r in range(0, n+1):
                B.append([])
                for i in range(0, r+1):
                    if r==0:
                        now = 1
                        B[r].append(now)
                    else:
                        now = 0
                        if i<=r-1:
                            now += (1-t)*B[r-1][i]
                        if i-1>=0:
                            now += t*B[r-1][i-1]
                        B[r].append(now)
                    if r == n:
                        x, y = 800 - 800*t, 800 - 800*B[r][i]
                        point = canva.create_oval(x-1, y-1, x, y, fill="#000000")
        

global curve
curve = Curve()


def main():
    global curve
    global degree
    degree = input("Please input a non-negative integer as the degree of Bernstein Polynomial.\n")
    degree = int(degree)
    # some initial setting
    window = tk.Tk()
    window.title('Bezier Curve')
    window.geometry('800x800')
    canva = tk.Canvas(window, width=800, height=800)

    canva.pack()
    curve.draw_bezier(canva)

    window.mainloop()
    

if __name__ == '__main__':
    main()
