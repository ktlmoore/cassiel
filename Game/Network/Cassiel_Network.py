###############################################################
# Cassiel_Network.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

from Network.Cassiel_Msg import Cassiel_Msg
from Network.Cassiel_NetIDs import NetID

###############################################################
# Class

class Cassiel_Network:

	clients = {}
	isServer = False
	server = None

	@staticmethod
	def addClient(client, id):
		Cassiel_Network.clients[id] = client
	
	
	@staticmethod
	def sendMessage(msg):
		# Send a message	
		# Case by destination
		to = msg.dst
		if (to == NetID.SERVER):
			# Sending to the server
			if (Cassiel_Network.isServer):
				# If we are the server, handle it
				Cassiel_Network.server.handleMessage(msg)
			else:
				# Otherwise send it via the Net
				print "bar"
