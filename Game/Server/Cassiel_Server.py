###############################################################
# Cassiel_Server.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import time
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
	
	lastFrameStamp = 0
	
	fooTimer = 1.0
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.lastFrameStamp = time.time()
	
	def run(self):
		while not self.done:
			self._update()
	
	def _update(self):
		# Work out delta time and cause a global update based on that time change
		thisFrameStamp = time.time()
		dt = (thisFrameStamp - self.lastFrameStamp)
		self.lastFrameStamp = thisFrameStamp
		self.update(dt)
	
	def update(self, dt):
		self.fooTimer -= dt
		if (self.fooTimer <= 0.0):
			print "foo"
			self.fooTimer = 1.0
		
	def handleMessage(self, msg):
		# Handle a message we've received
		if (msg.msgID is Cassiel_MsgID.ECHO):
			respMsg = Cassiel_Network.createMsg(id, msg.src, Cassiel_MsgType.RESPONSE, msg.data, Cassiel_MsgID.ECHO)
			Cassiel_Network.sendMessage(respMsg)
		elif (msg.msgID is Cassiel_MsgID.EXIT):
			respMsg = Cassiel_Network.createMsg(id, msg.src, Cassiel_MsgType.COMMAND, msg.data, Cassiel_MsgID.EXIT)
			Cassiel_Network.sendMessage(respMsg)
			self.done = True
		
	@staticmethod
	def toString():
		return "Server::"