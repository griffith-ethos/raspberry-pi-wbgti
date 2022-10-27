import tkinter as tk

from pages.temperature_display import TemperatureDisplay
from pages.settings_page import SettingsPage

class Root(tk.Tk):
	def __init__(self):
		super(Root,self).__init__()

		self.title("WBGTI")
		self.attributes("-fullscreen", True)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (TemperatureDisplay, SettingsPage):
			frame = F(container, self)
			self.frames[F.__name__] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("TemperatureDisplay")

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

root = Root()

root.mainloop()
