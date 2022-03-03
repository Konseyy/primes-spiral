from tkinter import *
import time

CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 1080
NODE_SIZE = 1
coord = {"x": CANVAS_WIDTH / 2, "y": CANVAS_HEIGHT / 2}
stepSize = NODE_SIZE * 2
totalPixels = (CANVAS_HEIGHT /
               (NODE_SIZE * 2))**2 if CANVAS_HEIGHT > CANVAS_WIDTH else (
                   CANVAS_WIDTH / (NODE_SIZE * 2))**2
master = Tk()

w = Canvas(master,
           width=CANVAS_WIDTH,
           height=CANVAS_HEIGHT,
           background="black")
w.pack()


def createBox(x, y, NODE_SIZE, fill):
	w.create_rectangle(x - NODE_SIZE,
	                   y - NODE_SIZE,
	                   x + NODE_SIZE,
	                   y + NODE_SIZE,
	                   fill=fill)


def sqrt(number):
	for i in range(number):
		if (i * i > number):
			return i
	return 0


def isPrime(num):
	if (num < 3):
		if (num == 2):
			return True
		return False
	if (num % 2 == 0):
		return False
	for i in range(3, sqrt(num) + 1, 2):
		if (num % i == 0):
			return False
	return True


lineLength = 1
timesLengthUsed = 0
direction = "right"
iterator = 0
i = 0
boxCoordinates = []
start = time.time()
while ((coord["x"] > 0 or coord["y"] > 0)
       and (coord["x"] < CANVAS_WIDTH or coord["y"] < CANVAS_HEIGHT)):
	i += 1
	if (not (coord["x"] < 0 or coord["y"] < 0 or coord["x"] > CANVAS_WIDTH
	         or coord["y"] > CANVAS_HEIGHT)):
		if (isPrime(i)):
			boxCoordinates.append({
			    "x": coord["x"],
			    "y": coord["y"],
			    "fill": "yellow"
			})
	iterator += 1
	if (direction == "right"):
		coord["x"] += stepSize
	elif (direction == "up"):
		coord["y"] -= stepSize
	elif (direction == "left"):
		coord["x"] -= stepSize
	elif (direction == "down"):
		coord["y"] += stepSize
	if (timesLengthUsed == 2):
		timesLengthUsed = 0
		lineLength += 1
	if (iterator == lineLength):
		timesLengthUsed += 1
		iterator = 0
		if (direction == "right"):
			direction = "up"
		elif (direction == "up"):
			direction = "left"
		elif (direction == "left"):
			direction = "down"
		elif (direction == "down"):
			direction = "right"
end = time.time()
print(f"Time elapsed (computation): ~{round(end-start,2)}s")
print(f"Nodes generated: {len(boxCoordinates)}")
print("Starting rendering")
for c in boxCoordinates:
	createBox(c["x"], c["y"], NODE_SIZE, c["fill"])
mainloop()
