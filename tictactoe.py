#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys

turn = 0
player = ""
positions = []

class tic_tac_toe:
	def delete_event(self, widget, event, data=None):	
		return False

	def popup(self, isTie=False):
	       	
		self.popup = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.popup.set_size_request(200,200)	
		self.ze_box = gtk.VBox(homogeneous=True, spacing=0)	
		self.popup.set_border_width(15)	
		global player		
		
		if isTie==True:
			self.label = gtk.Label("Game was a tie!")
			self.ze_box.pack_start(self.label)
		else :
			self.label = gtk.Label(player + " has won!")
			self.ze_box.pack_start(self.label)
			
		self.exit = gtk.Button("Exit")
		self.exit.connect("clicked", self.destroy, None)

		for e in positions:
			e.set_sensitive(False)

		self.ze_box.pack_start(self.exit)

		self.popup.add(self.ze_box)
		self.popup.show_all()
	
	def change(self, widget, data=None):
		global turn	
		global player

		# Checking if the label is not "" prevents a user from changing what the previous user put.
		if widget.get_label() == "":
			if turn%2 == 1:
				widget.set_label("X")
				player = "X"
				turn = turn + 1
		
			else :
				widget.set_label("O")	
				player = "O"
				turn = turn + 1
		
		elif widget.get_label() != "":
			pass	
		

		global positions
		# Check if any of the winning conditions is satisfied. This is a bit long and repetitive but I'm not sure of another way to 
		# do it for now aside from listing them all out
		
		if (positions[0].get_label() != "") and (positions[0].get_label() == positions[1].get_label() == positions[2].get_label()):
			self.popup()	

		elif (positions[3].get_label() != "") and (positions[3].get_label() == positions[4].get_label() == positions[5].get_label()):
			self.popup()	

		elif (positions[6].get_label() != "") and (positions[6].get_label() == positions[7].get_label() == positions[8].get_label()):
			self.popup()	

		elif (positions[0].get_label() != "") and (positions[0].get_label() == positions[3].get_label() == positions[6].get_label()):
			self.popup()	
	
		elif (positions[1].get_label() != "") and (positions[1].get_label() == positions[4].get_label() == positions[7].get_label()):
			self.popup()	
	
		elif (positions[2].get_label() != "") and (positions[2].get_label() == positions[5].get_label() == positions[8].get_label()):
			self.popup()	

		elif (positions[0].get_label() != "") and (positions[0].get_label() == positions[4].get_label() == positions[8].get_label()):
			self.popup()	
	
		elif (positions[2].get_label() != "") and (positions[2].get_label() == positions[4].get_label() == positions[6].get_label()):
			self.popup()	
		
		elif self.tie() == True:
			self.popup(True)	

	def tie(self):
		for e in positions:
			if e.get_label() == "":
				return False
		return True
	def destroy(self, widget, data=None):
		gtk.main_quit()
	
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_size_request(500, 500)
		winColor = gtk.gdk.color_parse('#0000FF')
		self.window.modify_bg(gtk.STATE_NORMAL, winColor)

		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)
		
		#Make an array with the buttons	
		for i in range(9):
			global positions
			positions.append(gtk.Button(""))

		for i in range(9):
			positions[i].connect("clicked", self.change, None)


		self.MainBox = gtk.VBox(homogeneous=True, spacing=3)
		self.box1 = gtk.HBox(homogeneous=True, spacing=3)	
		self.box2 = gtk.HBox(homogeneous=True, spacing=3)
		self.box3 = gtk.HBox(homogeneous=True, spacing=3)

		#Pack all the buttons into the boxes	
		for i in range(9):
			if i < 3:
				self.box1.pack_start(positions[i])
			if (i >= 3) and (i < 6):
				self.box2.pack_start(positions[i])
			if (i >= 6):
				self.box3.pack_start(positions[i])
				
		self.MainBox.pack_start(self.box1)
		self.MainBox.pack_start(self.box2)
		self.MainBox.pack_start(self.box3)

		self.window.add(self.MainBox)
		self.window.show_all()	

	def main(self):
		gtk.main()
print "Game in progress"
if __name__ == "__main__":
	game = tic_tac_toe()
	game.main()
