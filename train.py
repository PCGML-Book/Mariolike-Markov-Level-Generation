'''

This script collects the raw counts from the original Super Mario Bros. (SMB) and Super Mario Bros.: The Lost Levels (SMB2) levels 
and uses these to approximate the probability values of a Markov chain, which is saved to smbprobabilities.pickle.

This uses an L-shape Markov chain (right of Figure 6.7), where each tile value is assumed to be dependent on the tiles to the left, below, and to the 
left and below.

'''

import sys
import os
import glob
import pickle

levels = []#list of dictionaries, each dictionary a level

#Load SMB Levels into the levels list
for levelFile in glob.glob(os.path.join(os.getcwd(), "SMB1_Data", "Processed", "*.txt")):
	print ("Processing: "+levelFile) #print out which level is being loaded
	with open(levelFile) as fp:
		level = {}
		y = 0
		for line in fp:
			level[y] = line
			y+=1
		levels.append(level)

#Load SMB2 Levels into the levels list
for levelFile in glob.glob(os.path.join(os.getcwd(), "SMB2_Data", "Processed", "*.txt")):
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

			state = west+southwest+south

			if not state in markovCounts.keys():
				markovCounts[state] = {}
			if not level[y][x] in markovCounts[state].keys():
				markovCounts[state][level[y][x]] = 0

			#Increments the number of times we see the tile value at location (x,y) given the state (the tile values at (x-1, y), (x-1, y+1), (x, y+1))
			markovCounts[state][level[y][x]] +=1.0

#Normalize markov counts in order to approximate probability values
markovProbabilities = {} #The representation of our Markov chain, a dictionary of dictionaries 
for state in markovCounts.keys():
	markovProbabilities[state] = {}

	sumVal = 0
	for action in markovCounts[state].keys():
		sumVal+=markovCounts[state][action]
	for action in markovCounts[state].keys():
		markovProbabilities[state][action] =markovCounts[state][action]/sumVal #Approximation of probability values of seeing tile value 'action' given the current 'state'

#Save the 'markovProbabilities' dictionary to a file
pickle.dump(markovProbabilities, open("smbprobabilities.pickle", "wb"))



		


