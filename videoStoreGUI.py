"""
Program: videoStoreGUI.py
Author: Dominick Vera 07/10/2023

GUI- based version of the video store project from chapter 2

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly.

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
#Other imports go here

#Class header
class VideoStore(EasyFrame):
	# Definition of our class contructor method 
	def __init__(self):
		EasyFrame.__init__(self, title = "Buster Block", width = 340, height = 280, resizable = False, background = "MediumBlue")

		self.normalFont = Font(family = "Tahoma", size = 12)

		# Add various components to the window 
		self.addLabel(text = "Buster Block", row = 0, column = 0,columnspan = 2, sticky = "NSEW", foreground = "yellow", background = "MediumBlue", font = Font(family = "Ariel", size = 26))
		self.addLabel(text = "New Rentals: $3.00\n Old Rentals: $2.00", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "MediumBlue",foreground = "yellow", font = self.normalFont)

		self.addLabel(text = "# of New Rentals:", row = 2, column = 0, sticky = "NE", background = "MediumBlue",foreground = "yellow", font = self.normalFont)
		self.newRentals = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NW", width = 4)
		self.addLabel(text = "# of Old Rentals:", row = 3, column = 0, sticky = "NE", background = "MediumBlue", foreground = "yellow", font = self.normalFont)
		self.oldRentals = self.addIntegerField(value = 0, row = 3, column = 1, sticky = "NW", width = 4)

		# command button 
		self.button = self.addButton(text = "Check Out", row = 4, column = 0, columnspan = 2, command = self.checkOut)

		self.addLabel(text = "The total for the Order is:", row = 5, column = 0, sticky = "NE", background = "MediumBlue", font = self.normalFont, foreground = "yellow" )
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 10)

	# def of checkOut() function 
	def checkOut(self):
		#grab the user input from the GUI window 
		new = self.newRentals.getNumber()
		old = self.oldRentals.getNumber()

		#Processing phase aka the math
		result = (new * 3.00) + (old * 2.00)

		#Output phase

		self.total.setNumber(result)

# Definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()