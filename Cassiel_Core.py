###############################################################
# Cassiel_Core.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import sys
from Cassiel_Server import *

###############################################################
# Functions

def main(argv):
	server = Cassiel_Server()
	server.run()
    

if __name__ == "__main__":
    main(sys.argv)