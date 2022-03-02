from tkinter import *
import time
import math

CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 1080
NODE_SIZE = 1
RADIUS_STEP_SIZE = NODE_SIZE / 100
startCoord = {"x": CANVAS_WIDTH / 2, "y": CANVAS_HEIGHT / 2}
degreesStepSize = NODE_SIZE
colors = ("black", "yellow")
totalPixels = (CANVAS_HEIGHT /
               (NODE_SIZE * 2))**2 if CANVAS_HEIGHT > CANVAS_WIDTH else (
                   CANVAS_WIDTH / (NODE_SIZE * 2))**2
master = Tk()

w = Canvas(master,
           width=CANVAS_WIDTH,
           height=CANVAS_HEIGHT,
           background="black")
w.pack()


def createBox(x, y, NODE_SIZE, fill=colors[0]):
	w.create_rectangle(x - NODE_SIZE,
	                   y - NODE_SIZE,
	                   x + NODE_SIZE,
	                   y + NODE_SIZE,
	                   fill=fill)


def isPrime(num):
	if (num < 2):
		return False
	if (num == 2):
		return True
	if (num % 2 == 0):
		return False

	def sqrt(number):
		for i in range(number):
			if (i * i > number):
				return i
		return 0

	for i in range(3, sqrt(num) + 1, 2):
		if (num % i == 0):
			return False
	return True


i = 0
boxCoordinates = []
radius = 0
angle = 0
coord = startCoord
start = time.time()
while ((coord["x"] > 0 or coord["y"] > 0)
       and (coord["x"] < CANVAS_WIDTH or coord["y"] < CANVAS_HEIGHT)):
	# print(coord,angle,radius)
	i += 1
	if (coord["x"] > 0 and coord["y"] > 0) or (coord["x"] < CANVAS_WIDTH
	                                           and coord["y"] < CANVAS_HEIGHT):
		if (isPrime(i)):
			boxCoordinates.append({
			    "x": coord["x"],
			    "y": coord["y"],
			    "fill": colors[1] if isPrime(i) else colors[0]
			})
	coord = startCoord
	radius += RADIUS_STEP_SIZE
	angle += degreesStepSize
	# if (angle > 360): angle -= 360
	coord["x"] += radius * math.sin(angle)
	coord["y"] += radius * math.cos(angle)
end = time.time()
print(f"Time elapsed (computation): ~{round(end-start,2)}s")
print(f"Nodes generated: {len(boxCoordinates)}")
print("Starting rendering")
for c in boxCoordinates:
	createBox(c["x"], c["y"], NODE_SIZE, c["fill"])
mainloop()
