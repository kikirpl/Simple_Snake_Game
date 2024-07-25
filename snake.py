from ursina import *
app = Ursina()



def start():
  startBTN.visible = False

startBTN = Button(text='-: START :-',text_scale=2, color=color.black50, scale=(1 , 0.5), visible= True)
startBTN.on_click=start

snake = Entity(model='cube', texture='head.png', scale=0.4, z=-1, collider='box')
apple = Entity(texture='melon1.png',model='cube', scale=0.4, position=(1,-1,-1), collider='mesh')
body = [Entity(model='cube', scale =0.2, texture='body.png') for i in range(14)]

camera.orthographic = True
camera.fov = 8



from random import randint
dx = dy = 0


def update():
  info = snake.intersects()
  if info.hit:
    apple.x = randint(-4,4)/2
    apple.y = randint(-4,4)/2
    new = Entity(model='cube', z = -1, scale=0.2, texture='body.png')
    body.append(new)
  for i in range(len(body)-1,0,-1):
    pos = body[i-1].position
    body[i].position = pos
  body[0].x = snake.x
  body[0].y = snake.y
  snake.x += time.dt * dx
  snake.y += time.dt * dy


def input(key):
  global dx,dy
  for x,y,z in zip(['d','a'],[2,-2],[270,90]):
    if key==x:
      snake.rotation_z = z
      dx = y
      dy = 0
  for x,y,z in zip(['w','s'],[2,-2],[180,0]):
    if key == x:
      snake.rotation_z = z
      dy = y
      dx = 0


Sky(color=color.yellow)
app.run()