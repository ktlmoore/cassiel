###############################################################
# Cassiel_Server.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
from Game.Network.Cassiel_Msg import *
from Game.Network.Cassiel_NetIDs import *

class Cassiel_Server:
	def __init__(self):
		pass

	def run(self):
		msg = self.createMsg(0, NetID.ALL_CLIENTS)
		print msg.toString()
		
	def createMsg(self, id, dst):
		# Create a message with a given id and destination
		# and stamp it with our NetID
		msg = Cassiel_Msg(id, NetID.SERVER, dst)
		return msg