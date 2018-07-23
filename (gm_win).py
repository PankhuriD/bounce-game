from tkinter import*
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.dx = random.choice((-3,-2,-1,1,2,3))
        self.dy = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.pos = self.canvas.coords(self.id)

    def draw(self):
        self.canvas.move(self.id, self.dx, self.dy)
        self.pos = self.canvas.coords(self.id)
        if self.pos[1] <= 0:
            self.dy = 3
        elif self.pos[3] >= self.canvas_height:
            self.dy = -3
        if self.pos[0] <= 0:
            self.dx = -self.dx
        elif self.pos[2] >= self.canvas_width:
            self.dx = -self.dx

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10,
                                          fill=color)
        self.canvas.move(self.id, 200, 300)
        self.dx = 0
        self.canvas_width = self.canvas.winfo_width()
        self.pos = self.canvas.coords(self.id)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.dx, 0)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0] <= 0:
            self.dx = 0
        elif self.pos[2] >= self.canvas_width:
            self.dx = 0

    def turn_left(self, evt):
        if self.pos[0] > 0:
            self.dx = -3

    def turn_right(self, evt):
        if self.pos[2] < self.canvas_width:
            self.dx = 3
            
            

gm_win = Tk()
gm_win.title("Bounce!")
gm_win.resizable(0, 0)
gm_win.wm_attributes("-topmost", 1)
gm_canvas = Canvas(gm_win, width=500, height=400, bd=0, highlightthickness=0)
gm_canvas.pack()
gm_win.update()

ball = Ball(gm_canvas, "red")
paddle = Paddle(gm_canvas, "blue")

def hit_ball():
    if ball.pos[2] >= paddle.pos[0] and ball.pos[0] <= paddle.pos[2]:
        if ball.pos[3] >= paddle.pos[1] and ball.pos[3] <= paddle.pos[3]:
            ball.dy = -ball.dy
while True:
    ball.draw()
    paddle.draw()
    gm_win.update()
    hit_ball()
    if ball.pos[3] >= gm_canvas.winfo_height():
        break
    time.sleep(0.03)

gm_canvas.create_text(250, 150,
                       text="Game Over",
                       fill="green",
                       font=("Andalus", 75))
   
