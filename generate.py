'''

This script uses the Markov chain saved as a Python dictionary of dictionaries (smbprobabilities.pickle) to generate a new
level
'''

import sys
import os
import random
import pickle

#Load up the probability dictionary
markovProbabilities = pickle.load(open("smbprobabilities.pickle", "rb"))


level = {}

#Parameters determining the size of the level
maxY = 14 #will end up generating a level with one height larger than this
maxX = 100

#Starting in the bottom left corner, we begin the generation process, going bottom to top then left to right
for y in range(maxY, -1, -1):
	level[y] =""
	for x in range(0, maxX): #We generate one tile at a time for each iteration of this inner loop

		#Grab the current key, the three dependent values
		west = " "
		southwest = " "
		south = " "

		if x>0: 
			west = level[y][x-1]
		if y<maxY: 
			south = level[y+1][x-1]
		if x>0 and y<maxY: 
			southwest = level[y+1][x]

		key = west+southwest+south

		#Query the Markov chain to see what tile value we should place at this tile location
		if key in markovProbabilities.keys():
			
			#Greedy Sampling. 
			#Uncomment this and comment the Weighted Sampling section below to see what greedy sampling looks like (and why we don't tend to use it)
			'''
			maxValueTile = "-"
			maxValue = 0.0
			for key2 in markovProbabilities[key]:
				if markovProbabilities[key][key2] >maxValue:
					maxValue = markovProbabilities[key][key2]
					maxValueTile = key2
			level[y] +=maxValueTile #Add the tile value (tokenToUse) to the level
			'''
			#Weighted Sampling
			randValue = random.random()
			currProb = 0
			tokenToUse = "-"
			for key2 in markovProbabilities[key]:
				currProb+=markovProbabilities[key][key2]
				if currProb>randValue:
					tokenToUse = key2
					break
			
			level[y] += tokenToUse #Add the tile value (tokenToUse) to the level
			
		else:
			#If we can't find anything, just output an empty space
			level[y] +="-"

#Save the generated level to a file 
outputFile = open("./Generated Levels/output.txt", 'w')
for y in range(0, maxY+1):
   	outputFile.write(level[y]+"\n")
outputFile.close()
