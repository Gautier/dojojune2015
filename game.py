import math
import random

WIDTH = 800
HEIGHT = 600

alien = Actor('alien')
alien.drawme = True
egg = Actor('egg')
egg.drawme = False
score = 50
i = 0


def sigm(i):
    return 1. / (1.+math.exp(-i))


def draw():
    screen.clear()
    screen.fill((2, 128, 128))

    if alien.drawme:
        alien.draw()
    if egg.drawme:
        egg.draw()
    screen.draw.text('Score: {}'.format(score), topright=(WIDTH-5, 5))
    if score <= 0:
        screen.draw.text(
            'GAME OVER',
            bottomleft=((WIDTH / 2) - 50, HEIGHT / 2),
        )
        z()

def z():
    sounds.shoot.play()
    clock.schedule_unique(z, .1)

def spawn_alien():
    global score, alien, egg, i
    i += 1
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    egg.pos = alien.pos = x, y

    if random.randint(1, 10) > 8:
        egg.drawme = True
        alien.drawme = False
    else:
        egg.drawme = False
        alien.drawme = True

    score -= 1
    if score > 0:
        clock.schedule_unique(spawn_alien, 1.5 - (sigm(i-1.) / 5.))

spawn_alien()

def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        if alien.drawme:
            score += 1
            sounds.shoot.play()
        else:
            score -= 1
