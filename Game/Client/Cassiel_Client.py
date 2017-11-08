###############################################################
# Cassiel_Client.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import threading

from Network.Cassiel_Msg import Cassiel_Msg
from Network.Cassiel_Msg import Cassiel_MsgID
from Network.Cassiel_Network import Cassiel_Network
from Network.Cassiel_Network import NetID
from Window.Cassiel_Window import Cassiel_Window

###############################################################
# Class

class Cassiel_Client(threading.Thread):
	id = None
	window = None
	
	def __init__(self, id):
		self.window = Cassiel_Window(self)
		threading.Thread.__init__(self)
		self.id = id
		Cassiel_Network.addClient(self, id)
		
	def run(self):
		while not self.window.done:
			update()
		exitMsg = Cassiel_Network.createMsg(id, NetID.SERVER, "", Cassiel_MsgID.EXIT)
		Cassiel_Network.sendMessage(exitMsg)
		
	def update(self):
		pass
			
	def handleMessage(self, msg):
		msgID = msg.msgID
		if (msgID == Cassiel_MsgID.ECHO):
			print msg.data
		elif (msgID == Cassiel_MsgID.EXIT):
			self.done = True