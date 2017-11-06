###############################################################
# Cassiel_Network.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

from Game.Network.Cassiel_Msg import *
from Game.Network.Cassiel_NetIDs import *
from Game.Server.Cassiel_Server import *

import Cassiel_Core

###############################################################
# Class

class Cassiel_Network:
	
	@staticmethod
	def sendMessage(msg):
		# Send a message	
		# Case by destination
		to = msg.dst
		if (to == NetID.SERVER):
			# Sending to the server
			if (Cassiel_Core.isServer):
				# If we are the server, handle it
				Cassiel_Core.server.handleMessage(msg)
			else:
				# Otherwise send it via the Net
				print "bar"
