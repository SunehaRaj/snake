import tkinter
import random

COLUMNS = 25
ROWS = 25
TILESIZE = 25

WINDOW_HEIGHT = ROWS * TILESIZE
WINDOW_WIDTH = COLUMNS * TILESIZE

class Tile:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    
window = tkinter.Tk()
window.resizable(0,0)
window.title("SNAKE !!")

canvas = tkinter.Canvas(window, bg = "blue" , width = WINDOW_WIDTH , height = WINDOW_HEIGHT , borderwidth = False , highlightthickness=False )
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_pos = int((screen_width/2)-(window_width/2))
y_pos = int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

snake = Tile(TILESIZE*5 , TILESIZE*5)
food = Tile(TILESIZE*10 , TILESIZE*10)
s_body = []

velX = 0
velY = 0
Game_over = 0
score = 0
high_score=0

def direction_change(e):
    
    global velX , velY, Game_over, score, snake, food, s_body
    

    if (e.keysym == "Up" and velY != 1):
        velX = 0
        velY = -1
    elif (e.keysym == "Down" and velY != -1):
        velX = 0
        velY = 1
    elif (e.keysym == "Right" and velX != -1):
        velX = 1
        velY = 0
    elif (e.keysym == "Left" and velX != 1):
        velX = -1
        velY = 0
    elif (e.keysym == "space" and Game_over):
        velX =0
        velY=0
        score=0
        s_body = []
        snake = Tile(TILESIZE*5 , TILESIZE*5)
        food = Tile(TILESIZE*10 , TILESIZE*10)
        Game_over = 0   
    
  
def moving ():
  global snake, food, s_body, Game_over, score, high_score
  if(Game_over):
     return
  
  if(snake.x < 0 or snake.x>= WINDOW_WIDTH or snake.y<0 or snake.y>= WINDOW_HEIGHT ):
     Game_over = True
     return
     
  for tile in s_body:
     if (snake.x == tile.x and snake.y == tile.y):
        Game_over = True
        return
        
  if (snake.x == food.x and snake.y == food.y):
    s_body.append(Tile(food.x , food.y))
    food.x = random.randint (False , COLUMNS-1) * TILESIZE
    food.y = random.randint (False , ROWS-1) * TILESIZE
    score += 1
    if(score > high_score):
       high_score = score
    else:
       high_score   
 
  for i in range(len(s_body)-1, -1, -1):
    tile = s_body[i]
    
    if (i==0):
      tile.x = snake.x
      tile.y = snake.y
    else:
      prev_tile = s_body[i-1]
      tile.x = prev_tile.x
      tile.y = prev_tile.y
            
  
  snake.x += velX * TILESIZE
  snake.y += velY * TILESIZE

    


def drawing():
    global snake, food, s_body, Game_over, score

    moving()

    canvas.delete("all")

    canvas.create_rectangle(food.x , food.y , food.x + TILESIZE , food.y + TILESIZE , fill = "red")


    canvas.create_rectangle(snake.x , snake.y , snake.x + TILESIZE , snake.y + TILESIZE , fill = "yellow")

    for tile in s_body:
        canvas.create_rectangle(tile.x , tile.y , tile.x + TILESIZE , tile.y + TILESIZE , fill = "yellow")
        

    if (Game_over):
       canvas.delete ("all")
       

       canvas.create_text(WINDOW_WIDTH/2 , WINDOW_HEIGHT/2, font ="Arial 20", text = f"GAME OVER ! : {score}", fill = "white")
       canvas.create_text(310 , 390, font ="Arial 30", text = f"High Score ! : {high_score}", fill = "white")
       canvas.create_text(310 , 440, font ="Arial 20", text = f"Press space to restart", fill = "black")
        
       
    else:
       canvas.create_text(30,20, font = "Arial 10", text = f"Score : {score}", fill = "white")
       canvas.create_text(40,40, font = "Arial 10", text = f"High Score : {high_score}", fill = "white")

    window.after(100 , drawing)


  


drawing()
window.bind("<KeyRelease>" , direction_change )

window.mainloop()
