from tkinter import *
import random
import winsound
#--------------------window setup-----------
window=Tk()
window.title("PING GAME")
window.resizable(False,False)
#window
WIDTH=800
HEIGHT=600
#-------------------objects------------------------
canvas=Canvas(window,height=HEIGHT,width=WIDTH,bg="black")
canvas.pack()
for i in range(0,HEIGHT,30):
    canvas.create_line(WIDTH//2,i,WIDTH//2,i+15,fill="white")
player_score=0
ai_score=0
start_text=canvas.create_text(WIDTH//2,HEIGHT//2,text="PING GAME\n PRESS SPACE TO START",fill="white",font=("Arial",30),justify="center")
score_text=canvas.create_text(WIDTH/2,30,text="0:0",fill="white",font=("Arial",24))

paddle=canvas.create_rectangle(50,250,70,350,fill="white")
paddle2=canvas.create_rectangle(730,250,750,350,fill="white")
#paddle2=canvas.create_rectangle(730,250,750,350,fill="white")
#paddle3=canvas.create_rectangle(350,50,450,70,fill="white")
#paddle4=canvas.create_rectangle(350,530,450,550,fill="white")
#(x1,y1,x2,y2) x2-x1 gives us the width y2-y1 is the height x1 is from the left width y1 from the top height
ball=canvas.create_oval(390,290,410,310,fill="red")

game_state="start"

def start_game(event):
    global game_state
    if game_state=="start":
        game_state="playing"
        canvas.delete(start_text)

window.bind("<space>",start_game)
#------------------ball movement variables---------------------
dx=8   #horizontal speed   move right 5 pixels every frame
dy=6   #vertical speed     move down 3 pixels every frame
#-----------------game loop function----------------------------
def move_ball():
    global dx,dy
    global game_state
    #move ball to dx and dy
    if game_state=="playing":
        canvas.move(ball, dx, dy)  # x+=dx  y+=dy

        # we have to bounce the ball only for vertical in horizontal collision we recentre the ball
        x1, y1, x2, y2 = canvas.coords(ball)
        # wall collision and score update only left and right walls for score
        global player_score, ai_score
        if x1 <= 0:
            ai_score += 1
            canvas.coords(ball, 390, 290, 410, 310)
            dx = 8
            dy=6
        if x2 >= WIDTH:
            player_score += 1
            canvas.coords(ball, 390, 290, 410, 310)
            dx = -8
            dy=-6
        canvas.itemconfig(score_text, text=f"{player_score}:{ai_score}")
        if player_score == 5:
            game_state = "game_over"
            canvas.create_text(WIDTH // 2, HEIGHT // 2, text="PLAYER WINS", fill="yellow", font=("Arial", 40))
        if ai_score == 5:
            game_state = "game_over"
            canvas.create_text(WIDTH // 2, HEIGHT // 2,
                               text="AI WINS",
                               fill="red",
                               font=("Arial", 40))

        # ----------top and bottom  wall bounce---------------------
        if y1 <= 0 or y2 >= HEIGHT:
            dy = -dy
        # -------ball and paddle collision-----------
        # ------------paddle 1 collison-------------
        ball_pos = canvas.coords(ball)
        paddle_pos = canvas.coords(paddle)
        bx1, by1, bx2, by2 = ball_pos
        px1, py1, px2, py2 = paddle_pos
        if dx < 0 and bx2 >= px1 and bx1 <= px2 and by2 >= py1 and by1 <= py2:
            winsound.Beep(600, 50)
            dx = -dx
            dx *= 1.02
            dy *= 1.02
            MAX_SPEED = 15
            if abs(dx) > MAX_SPEED:
                if dx > 0:
                    dx = MAX_SPEED
                else:
                    dx = -MAX_SPEED
            if abs(dy) > MAX_SPEED:
                if dy > 0:
                    dy = MAX_SPEED
                else:
                    dy = -MAX_SPEED

        # ---------paddle 2 collision---------------------
        ball2_pos = canvas.coords(ball)
        paddle2_pos = canvas.coords(paddle2)
        bbx1, bby1, bbx2, bby2 = ball2_pos
        ppx1, ppy1, ppx2, ppy2 = paddle2_pos
        ball_center = ((bby1 + bby2) / 2) + random.randint(-20, 20)
        paddle_center = (ppy1 + ppy2) / 2
        if dx > 0 and bbx2 >= ppx1 and bbx1 <= ppx2 and bby1 <= ppy2 and bby2 >= ppy1:
            winsound.Beep(600, 50)
            dx = -dx
        # ----------------AI movement-------------------------
        AI_SPEED = 5
        if dx > 0:
            if paddle_center < ball_center and ppy2 < HEIGHT:
                canvas.move(paddle2, 0, AI_SPEED)
            elif paddle_center > ball_center and ppy1 > 0:
                canvas.move(paddle2, 0, -AI_SPEED)



    #call this function after every 20 ms means 50 frames per second
    window.after(20,move_ball)


def toggle_pause(event):
    global game_state
    if game_state=="playing":
        game_state="paused"
    elif game_state=="paused":
        game_state="playing"
window.bind("<p>",toggle_pause)
#---------------paddle movement------------------------------
PADDLE_SPEED=25
def move_paddle(event):
    x1,y1,x2,y2=canvas.coords(paddle)
    if (event.keysym=="w" or event.keysym=="Up") and y1>0:
        canvas.move(paddle,0,-PADDLE_SPEED)
    if (event.keysym=="s" or event.keysym=="Down") and y2<HEIGHT:
        canvas.move(paddle,0,PADDLE_SPEED)

#bind keys
window.bind("<w>",move_paddle)
window.bind("<s>",move_paddle)
window.bind("<Up>",move_paddle)
window.bind("<Down>",move_paddle)

move_ball()  #start movement
window.mainloop()

