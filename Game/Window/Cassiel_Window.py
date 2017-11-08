###############################################################
# Cassiel_Client.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import pyglet

###############################################################
# Class

class Cassiel_Window(pyglet.window.Window):
	
	ownerClient = None
	done = False
	
	def __init__(self, ownerClient):
		super(Cassiel_Window, self).__init__()
		self.label = pyglet.text.Label("Hello, world!")
		self.ownerClient = ownerClient
		
	def on_draw(self):
		self.clear()
		self.label.draw()
		
	def on_close(self):
		self.done = True
		super(Cassiel_Window, self).on_close()