'''

This script collects the raw counts from the original Super Mario Bros. (SMB) and Super Mario Bros.: The Lost Levels (SMB2) levels 
and uses these to approximate the probability values of a Markov chain, which is saved to smbprobabilities.pickle.

This uses an L-shape Markov chain, where each tile value is assumed to be dependent on the tiles to the left, below, and to the 
left and below.

'''

import sys
import os
import glob
import pickle

levels = []#list of dictionaries, each dictionary a level

#Load SMB Levels into the levels list
for levelFile in glob.glob("./SMB1_Data/Processed/*.txt"):
	print ("Processing: "+levelFile) #print out which level is being loaded
	with open(levelFile) as fp:
		level = {}
		y = 0
		for line in fp:
			level[y] = line
			y+=1
		levels.append(level)

#Load SMB2 Levels into the levels list
for levelFile in glob.glob("./SMB2_Data/Processed/*.txt"):
	print ("Processing: "+levelFile) #print out which level is being loaded
	with open(levelFile) as fp:
		level = {}
		y = 0
		for line in fp:
			level[y] = line
			y+=1
		levels.append(level)

#Extract Markov chain Counts from 'levels'
markovCounts = {}#Dictionary of (x-1, y), (x-1, y+1), (x, y+1)
for level in levels: #Looking at one level at a time
	maxY = len(level)-1
	for y in range(maxY, -1, -1):
		for x in range(0, len(level[y])-1):

			#This grabs the tile values to the left (west), below (south), and left and below (southwest)
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

			if not key in markovCounts.keys():
				markovCounts[key] = {}
			if not level[y][x] in markovCounts[key].keys():
				markovCounts[key][level[y][x]] = 0

			#Increments the number of times we see the tile value at location (x,y) in this specific level
			markovCounts[key][level[y][x]] +=1.0

#Normalize markov counts in order to approximate probability values
markovProbabilities = {} #The representation of our Markov chain, a dictionary of dictionaries 
for key in markovCounts.keys():
	markovProbabilities[key] = {}

	sumVal = 0
	for key2 in markovCounts[key].keys():
		sumVal+=markovCounts[key][key2]
	for key2 in markovCounts[key].keys():
		markovProbabilities[key][key2] =markovCounts[key][key2]/sumVal #Approximation of probability values of seeing tile value 'key2' given key

#Save the 'markovProbabilities' dictionary to a file
pickle.dump(markovProbabilities, open("smbprobabilities.pickle", "wb"))



		


