###############################################################
# Cassiel_Core.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import sys

from Network.Cassiel_NetIDs import NetID
from Server.Cassiel_Server import Cassiel_Server
from Client.Cassiel_Client import Cassiel_Client
from Network.Cassiel_Network import Cassiel_Network

###############################################################
# Functions

isServer = True
server = None

def main(argv):
	# Handle arguments
	for arg in argv[1:]:
		if (arg == "-s"):
			Cassiel_Network.isServer = True
		elif (arg == "-c"):
			Cassiel_Network.isServer = False
			
	# Set up client and run it		
	
	# Set up server and run it
	if (isServer):
		client = Cassiel_Client(NetID.FIRST_CLIENT)
		Cassiel_Network.server = Cassiel_Server()
		Cassiel_Network.server.run()

if __name__ == "__main__":
    main(sys.argv)