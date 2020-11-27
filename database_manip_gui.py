import tkinter as tk
from database_interaction import Database

class MainApp(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.master = master
		self.configure_gui()
		self.create_widgets()

	def configure_gui(self):
		self.master.title("Test Application")
		self.master.geometry("500x500")
		self.master.resizable(False, False)

	def create_widgets(self):
		d_b = Database("test.db")
		print(d_b)

	def exit_program(self):
		exit(0)

if __name__ == "__main__":
	root = tk.Tk()
	main_app = MainApp(root)
	root.mainloop()
