# Mariolike Markov Level Generation
An example of using a Markov chain to generate levels like those from Super Mario Bros. based on the Markov chain given on the right side of Figure 6.7

Scripts:

-train.py: code that trains a Markov chain on the levels from Super Mario Bros. 1 and 2 (The Lost Levels)
-generate.py: code that generates a new level from the trained Markov chain, overwriting the existing level
-visualize.py: code that visualizes the generated level with assets from Kenney's Platformer Asset Pack

To run the code take the following steps: 

1. Install Python 3.9 (but tweaking it for other versions should be simple) and the 'pickle' library
2. Run train.py, which will train a Markov chain represented as a dictionary of dictionaries based on the levels from Super Mario Bros. (SMB) and Super Mario Bros.: The Lost Levels (SMB2)
3. Run generate.py, which will generate a level in a tile representation to Generated Levels/output.txt (Warning: this will overwrite any previous generated levels)
4. (Optionally) run visualize.py, which will visualize the generated level using Kenney's Pixel Platformer assets.
5. Make alterations to train.py to alter the state representation of the Markov chain, generate.py to alter the sampling procedure, or visualize.py to alter the visualization procedure including the constructive rules, rereun steps 2-4 to see the impact of these changes
