'''

Script for visualizing the generated output.txt levels

'''
import sys
import os
import glob
from PIL import Image #Need to import this to do image editing

#Load the set of all sprites
sprites = {}
for filename in glob.glob(os.path.join(os.getcwd(), "sprites", "*.png")):
	im = Image.open(filename)
	splits = filename.split("/")
	name = splits[-1][:-4]
	sprites[name] = im.convert('RGBA')

#This gives the mapping between the tile values and the associated sprite
visualization = {}
visualization["S"] = "brick"
visualization["?"] = "exclamationBox"
visualization["Q"] = "exclamationBoxEmpty"
visualization["E"] = "enemy"
visualization["<"] = "bushTopLeft"
visualization[">"] = "bushTopRight"
visualization["["] = "bushLeft"
visualization["]"] = "bushRight"
visualization["o"] = "coin"
visualization["B"] = "arrowTop"
visualization["b"] = "arrowBottom"

# This reads in the level
level = {}
with open(os.path.join(os.getcwd(), "Generated Levels", "output.txt")) as fp:
	y = 0
	for line in fp:
		level[y] = line
		y+=1

#Multiply by 18 here as each of the sprites is 18*18
image = Image.new("RGB", (18*len(level[0]), 18*len(level.keys())), color=(223, 245, 244)) #This creates an initially blank image for the level
pixels = image.load() #This loads the level image's pixels so we can edit them

maxY = len(level.keys())
maxX = len(level[0])

for y in range(0, maxY):
	for x in range(0, maxX):
		imageToUse = None
		if level[y][x] in visualization.keys():
			imageToUse = sprites[visualization[level[y][x]]]
		elif level[y][x]=="X":
			#Rules we've added to ensure the correct sprite is used
			if y==maxY-2:
				imageToUse = sprites["groundTop"]
			elif y==maxY-1:
				#Check if we have a solid tile above this and change which sprite we use if so
				if level[y-1][x]=="X":
					imageToUse = sprites["groundBottom"]
				else:
					imageToUse = sprites["groundTop"]
			else:
				imageToUse = sprites["stair"]

		if not imageToUse == None:
			#If we have a sprite (imageToUse) copy its pixels over
			pixelsToUse = imageToUse.load()
			for x2 in range(0, 18):
				for y2 in range(0, 18):
					if pixelsToUse[x2,y2][3]>0:
						pixels[x*18+x2,y*18+y2] = pixelsToUse[x2,y2][0:-1]

#Save the output to a jpeg
image.save("output.jpeg", "JPEG")
