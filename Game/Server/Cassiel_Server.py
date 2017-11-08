###############################################################
# Cassiel_Server.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import threading

from Network.Cassiel_Msg import Cassiel_Msg
from Network.Cassiel_Msg import Cassiel_MsgID
from Network.Cassiel_Msg import Cassiel_MsgType
from Network.Cassiel_NetIDs import NetID
from Network.Cassiel_Network import Cassiel_Network

###############################################################
# Class

class Cassiel_Server(threading.Thread):
	name = "SERVER"
	done = False
	id = NetID.SERVER
	
	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		pass
		
	def send(self, msg):
		# Send a message via the Network
		pass
		
	def handleMessage(self, msg):
		# Handle a message we've received
		if (msg.msgID is Cassiel_MsgID.ECHO):
			respMsg = Cassiel_Network.createMsg(id, msg.src, Cassiel_MsgType.RESPONSE, msg.data, Cassiel_MsgID.ECHO)
			Cassiel_Network.sendMessage(respMsg)
		elif (msg.msgID is Cassiel_MsgID.EXIT):
			respMsg = Cassiel_Network.createMsg(id, msg.src, Cassiel_MsgType.COMMAND, msg.data, Cassiel_MsgID.EXIT)
			Cassiel_Network.sendMessage(respMsg)
		
	@staticmethod
	def toString():
		return "Server::"