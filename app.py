#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from tkinter import *
import pickle
import datetime as dt
import os
import time

DATABASEFILE = 'weight.db'

# TODO:
# make a class --- DONE
# add date field
# add a button to show the plot in a separate window -- DONE
# resize the window -- DONE

class WeightTracker(Frame):

	def __init__(self):

		# main frame
		Frame.__init__(self, width=700, height=700)
		self.pack()
		self.master.title('Weight Tracker')
		self.master.iconname("calc1")

		# entry frame
		entry_frame = Frame(self, relief=GROOVE, borderwidth=2)
		display = DoubleVar()
		#display.set(0.0)
		self.entry_weight = Entry(entry_frame, relief=SUNKEN, textvariable = display)
		self.entry_weight.pack(side=LEFT, expand=NO,fill=BOTH)
		Button(entry_frame, text="Submit", command=lambda: self.add_entry()).pack(side=RIGHT, padx=20, pady=8)
		entry_frame.place(relx=0.2, rely=0.05, anchor=NW)
		Label(self, text='Enter your weight').place(relx=.26, rely=0.05, anchor=W)
		
		# show plot button
		Button(self, text="Show plot", command=lambda: plt.show()).place(relx=.7, rely=0.08, anchor=W)

		# plot frame
		plot_frame = Frame(self, relief=GROOVE, borderwidth=2)
		self.canvas=Canvas(plot_frame, width=640, height=480 )
		self.produce_plot()
		img = PhotoImage(file='fig.png')
		self.canv_image = self.canvas.create_image(0,0, image=img, anchor=NW)
		self.canvas.image = img # http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
		self.canvas.pack()
		plot_frame.place(relx=0.01, rely=0.15, anchor=NW)

	def add_entry(self):
		data = pickle.load(open(DATABASEFILE,'rb'))
		date = dt.datetime.now().date()
		weight = float(self.entry_weight.get())
		entry = (date, weight)
		print('INFO: adding', entry, 'to ', DATABASEFILE)
		data.append(entry)
		pickle.dump(data, open(DATABASEFILE,'wb'))
		self.produce_plot()
		img = PhotoImage(file='fig.png')
		self.canvas.itemconfigure(self.canv_image, image = img)
		self.canvas.image = img # http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm

	def produce_plot(self):
		data = pickle.load(open(DATABASEFILE,'rb'))
		dates = [x[0] for x in data]
		weights = [x[1] for x in data]
		for x in data:
			print(x)

		#plt.close()
		plt.figure()
		plt.plot(dates, weights, 'o')
		plt.ylabel('Weight [kg]')
		plt.savefig("fig.png")

if __name__ == '__main__':
	WeightTracker().mainloop()
	print('out of mainloop')
