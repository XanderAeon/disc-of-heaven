from adafruit_circuitplayground import cp
import time
import math

print("ha ha lmao")
true = True
false = False
count = 0

pixelstates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class g:
    merry = "christmas"

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
        global gameobjects
        gameobjects.remove(me)

def draw_led(x, y, color):
    if y > 4 or x > 1 or y < 0 or x < 0:
        return false
    if x == 1:
        pixelstates[4-y] = color
    else:
        pixelstates[5+y] = color
    return true

def main():
    while true:
        i = 0
        while i < 10:
            pixelstates[i] = (0, 0, 0)
            i += 1
        i = 0
        while i < len(gameobjects):
            gameobjects[i].step()
            left_pressed()
            right_pressed()
            i += 1
        i = 0
        while i < len(gameobjects):
            gameobjects[i].draw()
            i += 1
        i = 0
        while i < 10:
            cp.pixels[i] = pixelstates[i]
            i += 1
        time.sleep(1/60)

def c_null():
    return undefined

but_left = false
but_right = false

def left_pressed():
    global but_left
    if cp.button_b:
        if but_left:
            return false
        but_left = true
        return true
    but_left = false
    return false

def right_pressed():
    global but_right
    if cp.button_a:
        if but_right:
            return false
        but_right = true
        return true
    but_right = false
    return false


class menu(gameobject):
    x = -1
    y = 0
    def step(farting):
        if right_pressed():
            instance_create(0, 4, note, (10, 10, 10))

class note(gameobject):
    x = 0
    y = 5
    def step(me):
        me.y -= .1
        print(left_pressed())
        print(right_pressed())
        if me.y < 0:
            instance_create(me.x, 0, redpart, (10, 0, 0))
            me.destroy()
        elif me.y < .5 and cp.button_b:
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
    gameobjects.append(chump)
    chump.x = x
    chump.y = y
    chump.color = color

gameobjects = [
menu()
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
