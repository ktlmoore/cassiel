###############################################################
# Cassiel_Msg.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

import time
from enum import IntEnum

###############################################################
# Class
	
class Cassiel_MsgID(IntEnum):
	NONE = 0,
	ECHO = 1,
	EXIT = 2

class Cassiel_Msg:
	id = None
	src = None
	dst = None
	time = None
	type = None
	data = None
	msgID = Cassiel_MsgID.NONE
	
	nextId = 0
	
	def __init__(self, src, dst, msgID):
		self.id = Cassiel_Msg.nextId
		Cassiel_Msg.nextId += 1
		self.src = src
		self.dst = dst
		self.time = time.time()
		self.msgID = msgID
	
	def toString(self):
		return "Msg::[ID: {}, Src: {}, Dst: {}, Time: {}]\n''{}''".format(self.id, self.src, self.dst, self.time, self.data)
		
	def setData(self, data):
		self.data = data