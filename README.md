# Mariolike-Markov-Level-Generation
An example of using a Markov chain to generate levels like those from Super Mario Bros.

This example is written in Python, and should work for any Python version. 

To run the code take the following steps: 

1. Download and install Python
2. Install the Python libraries pickle and PIL, we recommend using pip!
3. Run train.py, which will construct a Markov chain represented as a dictionary of dictionaries based on the levels from Super Mario Bros. (SMB) and Super Mario Bros.: The Lost Levels (SMB2)
4. Run generate.py, which will generate a level in a tile representation to Generated Levels/output.txt (Warning: this will overwrite any previous generated levels)
5. (Optionally) run visualize.py, which will visualize the generated level using Kenney's Pixel Platformer assets.
