###############################################################
# Cassiel_Server.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import threading

from Network.Cassiel_Msg import Cassiel_Msg
from Network.Cassiel_Msg import Cassiel_MsgType
from Network.Cassiel_Msg import Cassiel_MsgID
from Network.Cassiel_Network import Cassiel_Network
from Network.Cassiel_Network import NetID

###############################################################
# Class

class Cassiel_Client(threading.Thread):
	id = None
	done = False
	
	def __init__(self, id):
		threading.Thread.__init__(self)
		self.id = id
		Cassiel_Network.addClient(self, id)
		
	def run(self):
		# Run the client loop
		while not self.done:
			cmd = raw_input("@ ")
			
			msgID = Cassiel_MsgID.ECHO
			if (cmd == "exit"):
				msgID = Cassiel_MsgID.EXIT
			
			msg = Cassiel_Network.createMsg(self.id, NetID.SERVER, Cassiel_MsgType.REQUEST, cmd, msgID)
			Cassiel_Network.sendMessage(msg)
			
	def handleMessage(self, msg):
		msgID = msg.msgID
		if (msgID == Cassiel_MsgID.ECHO):
			print msg.data
		elif (msgID == Cassiel_MsgID.EXIT):
			self.done = True