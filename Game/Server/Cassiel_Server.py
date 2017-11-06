###############################################################
# Cassiel_Server.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

from Network.Cassiel_Msg import Cassiel_Msg
from Network.Cassiel_NetIDs import NetID
from Network.Cassiel_Network import Cassiel_Network

###############################################################
# Class

class Cassiel_Server:
	name = "SERVER"
	done = False
	
	def run(self):
		while not self.done:
			cmd = raw_input("@ ")
			msg = self.createMsg(cmd, NetID.SERVER)
			Cassiel_Network.sendMessage(msg)
		
	def createMsg(self, id, dst):
		# Create a message with a given id and destination
		# and stamp it with our NetID
		msg = Cassiel_Msg(id, NetID.SERVER, dst)
		return msg
		
	def send(self, msg):
		# Send a message via the Network
		pass
		
	def handleMessage(self, msg):
		# Handle a message we've received
		print msg.toString()
		if (msg.id == "done"):
			self.done = True
		
	@staticmethod
	def toString():
		return "Server::"