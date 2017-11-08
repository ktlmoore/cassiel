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

	firstClientID = 0
	lastClientID = 0
	clients = {}
	isServer = False
	server = None
	
	@staticmethod
	def addClient(client, id):
		Cassiel_Network.clients[id] = client
		if (len(Cassiel_Network.clients) == 0):
			Cassiel_Network.firstClientID = id
		if (id > Cassiel_Network.lastClientID):
			Cassiel_Network.lastClientID = id
	
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
		elif (to >= Cassiel_Network.firstClientID and to <= Cassiel_Network.lastClientID):
			# Sending to a client
			Cassiel_Network.clients[to].handleMessage(msg)
				
	@staticmethod
	def createMsg(src, dst, type, data, msgID):
		# Create a message with given source, dest, type, data and msgID
		msg = Cassiel_Msg(src, dst, type, msgID)
		msg.setData(data)
		return msg
