from adafruit_circuitplayground import cp
import time
import math

print("ha ha lmao")
true = True
false = False
count = 0



class g:
    merry = "christmas"

g.pixelstates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g.count = 40
print(g.count)

def sinmult(val, duration, multiplier):
    return math.sin(val/duration)*multiplier


class gameobject:
    count = 0
    iterations = 0
    color = (10, 10, 10)
    x = -1
    y = -1
    brightness = 1
    def step(me):
        print("impostor")
    def draw(me):
        brightmult = abs(me.y%1-.5)
        r = me.color[0]*me.brightness*brightmult
        g = me.color[1]*me.brightness*brightmult
        b = me.color[2]*me.brightness*brightmult
        draw_led(round(me.x), round(me.y), (r, g, b))
    def destroy(me):
        g.gameobjects.remove(me)

def draw_led(x, y, color):
    if y > 4 or x > 1 or y < 0 or x < 0:
        return false
    if x == 1:
        g.pixelstates[4-y] = color
    else:
        g.pixelstates[5+y] = color
    return true

def main():
    while true:
        i = 0
        input()
        while i < 10:
            g.pixelstates[i] = (0, 0, 0)
            i += 1
        i = 0
        while i < len(g.gameobjects):
            g.gameobjects[i].step()
            i += 1
        i = 0
        while i < len(g.gameobjects):
            g.gameobjects[i].draw()
            i += 1
        i = 0
        while i < 10:
            cp.pixels[i] = g.pixelstates[i]
            i += 1
        time.sleep(1/60)

def c_null():
    return undefined

class input:
    hit = 0
    held = 0
    drop = 0

g.left = input()
g.right = input()
def right_pressed():
    if cp.button_a:
        if g.but_right:
            return false
        g.but_right = true
        return true
    g.but_right = false
    return false

def input():

    if cp.button_a:
        if g.right.held >= 1:
            g.right.hit = 0
        else:
            print("righted")
            g.right.hit = 1
        g.right.held += 1
    elif g.right.held >= 1:
        g.right.held = 0
        g.right.drop = 1
        g.right.hit = 0
    else:
        g.right.held = 0
        g.right.drop = 0
        g.right.hit = 0

    if cp.button_b:
        if g.left.held >= 1:
            g.left.hit = 0
        else:
            print("lefted")
            g.left.hit = 1
        g.left.held += 1
    elif g.left.held >= 1:
        g.left.held = 0
        g.left.drop = 1
        g.left.hit = 0
    else:
        g.left.held = 0
        g.left.drop = 0
        g.left.hit = 0

class menu(gameobject):
    x = -1
    y = 0
    def step(farting):
        if g.right.hit:
            instance_create(0, 4, note, (10, 10, 10))

class note(gameobject):
    x = 0
    y = 5
    def step(me):
        me.y -= .1
        if me.y < 0:
            instance_create(me.x, 0, redpart, (10, 0, 0))
            me.destroy()
        elif me.y < .5 and g.left.hit:
            print("he he lol")
            instance_create(me.x, 0, redpart, (0, 0, 10))
            me.destroy()

class redpart(gameobject):
    def step(me):
        me.brightness -= .1
        if me.brightness <= 0:
            me.destroy()

def instance_create(x, y, obj, color):
    global gameobjects
    chump = obj()
    g.gameobjects.append(chump)
    chump.x = x
    chump.y = y
    chump.color = color



class tone:
    def __init__(me, val, time):
        me.val = val
        me.time = time

class song(gameobject):
    notes = [
        tone(932, 1.0),
        tone(622, 1.2),
        tone(1244, 1.4),
        tone(1046, 1.6),
        tone(932, 1.8),
        tone(622, 2.0),
        tone(932, 2.2),
        tone(830, 2.4),
        tone(783, 2.6),
        tone(783, 2.8),
        tone(622, 3.0),
        tone(932, 3.2),
        tone(1244, 3.4),
        tone(1396, 3.6),
        tone(1567, 3.8),
    ]
    def step(me):
        me.count += 1.0
        i = 0
        #print("hey")
        if len(me.notes) <= 0:
            return
        #print(me.count, me.notes[0].time*60)
        while i<len(me.notes):
            break #delete for pwnage
            if me.count >= me.notes[i].time*60+.2*60:
                cp.stop_tone()
                me.notes.remove(me.notes[i])
            if len(me.notes) <= 0:
                break
            if me.count >= me.notes[i].time*60:
                print(me.notes[i].val)
                cp.start_tone(me.notes[i].val)
            i += 1

g.gameobjects = [
    menu(),
    song(),
]

main()


while true:
    cp.red_led = true
    #cp.pixels.fill((0, 0, 128+math.sin(count/30)*128))
    time.sleep(.01)
    count += 1
    j = 0
    while j<10:
        cp.pixels[j] = (0, 0, 10+sinmult(count+j*20, 5, 10))
        j += 1
