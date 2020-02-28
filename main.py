import pyglet
from util import *

win = pyglet.window.Window()
# Load the image & create the sprite
img = pyglet.image.load('assets/hero/sliced/idle-1.png')
spr = pyglet.sprite.Sprite(img, x = 100, y = 200)
spr.scale = 4

speed = -1


def update(dt):
  global speed
  spr.x += speed
  if spr.x < 100 or spr.x > 400:
    speed = speed * -1

@win.event
def on_draw():
  win.clear()
  pixelScale()

  spr.draw()

pyglet.clock.schedule_interval(update, 0.015)
pyglet.app.run()

