import pgzrun, time


background = Actor('background')

player = Actor('player')

WIDTH = 600
HEIGHT = 600

music.play('loading')

def draw():
    screen.clear()
    background.draw()
    player.draw()

def update():
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

def on_mouse_down(pos):
    if player.collidepoint(pos):
        set_alien_hurt()
    else:
        set_alien_normal()


def set_alien_hurt():
    print("Попав!")
    player.image = 'playerjump'
    sounds.scream.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    print("Мазило! Ха-ха-ха")
    player.image = 'player'



pgzrun.go()