###############################################################
# Cassiel_Core.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import sys
from Game.Server.Cassiel_Server import *

###############################################################
# Functions

isServer = True
server = None

def main(argv):
	Cassiel_Core.server = Cassiel_Server()
	
	Cassiel_Core.server.run()

if __name__ == "__main__":
    main(sys.argv)