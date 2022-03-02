from tkinter import *
import time

CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900
NODE_SIZE = 1.5
coord = {"x": CANVAS_WIDTH/2, "y": CANVAS_HEIGHT/2}
stepSize = NODE_SIZE*2
colors = ("black", "yellow")
totalPixels = (CANVAS_HEIGHT/(NODE_SIZE*2)
               )**2 if CANVAS_HEIGHT > CANVAS_WIDTH else (CANVAS_WIDTH/(NODE_SIZE*2))**2
master = Tk()

w = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
w.pack()


def createBox(x, y, NODE_SIZE, fill=colors[0]):
    w.create_rectangle(x-NODE_SIZE, y-NODE_SIZE, x +
                       NODE_SIZE, y+NODE_SIZE, fill=fill)


def isPrime(num):
    if(num < 2):
        return False
    if(num == 2):
        return True
    if(num % 2 == 0):
        return False

    def sqrt(number):
        for i in range(number):
            if(i*i > number):
                return i
        return 0
    for i in range(3, sqrt(num)+1, 2):
        if(num % i == 0):
            return False
    return True


lineLength = 1
timesLengthUsed = 0
direction = "right"
iterator = 0
i = 0
boxCoordinates = []
start = time.time()
while((coord["x"] > 0 or coord["y"] > 0) and (coord["x"] < CANVAS_WIDTH or coord["y"] < CANVAS_HEIGHT)):
    i += 1
    if(not(coord["x"] < 0 or coord["y"] < 0 or coord["x"] > CANVAS_WIDTH or coord["y"] > CANVAS_HEIGHT)):
        boxCoordinates.append(
            {"x": coord["x"], "y": coord["y"], "fill": colors[1] if isPrime(i) else colors[0]})
    iterator += 1
    if(direction == "right"):
        coord["x"] += stepSize
    elif(direction == "up"):
        coord["y"] -= stepSize
    elif(direction == "left"):
        coord["x"] -= stepSize
    elif(direction == "down"):
        coord["y"] += stepSize
    if(timesLengthUsed == 2):
        timesLengthUsed = 0
        lineLength += 1
    if(iterator == lineLength):
        timesLengthUsed += 1
        iterator = 0
        if(direction == "right"):
            direction = "up"
        elif(direction == "up"):
            direction = "left"
        elif(direction == "left"):
            direction = "down"
        elif(direction == "down"):
            direction = "right"
end = time.time()
print(f"Time elapsed (computation): ~{round(end-start,2)}s")
print(f"Nodes generated: {len(boxCoordinates)}")
print("Starting rendering")
for c in boxCoordinates:
    createBox(c["x"], c["y"], NODE_SIZE, c["fill"])
mainloop()
