import tkinter as tk

class Calculator:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("My calulator")
    
    def run(self):
        self.window.mainloop()
        
        
if __name__== "__main__":
    cal = Calculator()
    cal.run