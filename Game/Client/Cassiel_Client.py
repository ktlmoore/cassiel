###############################################################
# Cassiel_Server.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

from Network.Cassiel_Network import Cassiel_Network

###############################################################
# Class

class Cassiel_Client:
	id = None
	
	def __init__(self, id):
		self.id = id
		Cassiel_Network.addClient(self, id)
		
	