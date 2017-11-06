###############################################################
# Cassiel_Msg.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

import time

###############################################################
# Class

class Cassiel_Msg:
	id = None
	src = None
	dst = None
	time = None
	
	def __init__(self, id, src, dst):
		self.id = id
		self.src = src
		self.dst = dst
		self.time = time.time()
		
	def toString(self):
		return "Msg::[ID: {}, Src: {}, Dst: {}, Time: {}]".format(self.id, self.src, self.dst, self.time)
		
