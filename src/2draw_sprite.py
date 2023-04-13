import pgzrun, time

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20
alien.topright = 0, 10

music.play('loading')

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        set_alien_normal()


def set_alien_hurt():
    print("Попав!")
    alien.image = 'alien_hurt'
    sounds.scream.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    print("Мазило! Ха-ха-ха")
    alien.image = 'alien'



pgzrun.go()