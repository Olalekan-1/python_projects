#!/usr/bin/env python3

from tkinter import *

my_font = ("Arial", 17, "bold")
current_font = ("Arial", 45, "bold")
button_font = ("Arial", 30, "bold")

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("My Calculator")
        
        self.total_display = ""
        self.current_display = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.current_label = self.display()
        self.buttom_frame = self.create_button_frame()
        
        self.operators = {"/":"\u00F7", "*": "\u00D7", "+": "+", "-":"-"}
        
        self.digit = {7: (1, 1), 8: (1, 2), 9:(1,3),
                      4: (2, 1), 5:(2, 2), 6: (2, 3),
                      1: (3, 1), 2: (3, 2), 3: (3, 3),
                      0: (4, 2), ".": (4, 1)}
        self.display_digit()
        self.display_operator()
        self.create_special_button()
        #self.create_equal_button()
        
        self.buttom_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.buttom_frame.rowconfigure(i, weight=1)
            self.buttom_frame.columnconfigure(i, weight=1)
        self.bind_key()
        
    def create_display_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_button_frame(self):
        frame = Frame(self.window, height=65, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
        return frame
    
    def display(self):
        total_label = Label(self.display_frame, text=self.total_display, anchor=E, bg="gray",  height=1, font=my_font, padx=24)
        total_label.pack(expand=True, fill="both")
        
        current_label = Label(self.display_frame, text=self.current_display, anchor=E, bg="white", font=current_font, padx=24)
        current_label.pack(expand=True, fill="both")
        
        return total_label, current_label
    
    def expression(self, value):
        self.current_display += str(value)
        self.update_current_label()
        
    def display_digit(self):
        for digit, position in self.digit.items():
            button = Button(self.buttom_frame, text=str(digit), bg="white", fg="black", border=0, font=button_font, command=lambda x=digit: self.expression(x))
            button.grid(row=position[0], column=position[1], sticky=NSEW)
            
    def add_operator(self, value):
        #self.total_display += self.current_display 
        self.current_display += value
        self.total_display += self.current_display
        #self.update_current_label()
        self.current_display = ""
        #self.update_current_label()
        self.update_total_label()
        self.update_current_label()
    
    def display_operator(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = Button(self.buttom_frame, text=symbol, bg="white", fg="black", borderwidth=0, font=button_font, command=lambda x=operator: self.add_operator(x))
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1
            
    def set_equal(self):
        try:
            self.total_display += self.current_display
            self.update_total_label()
            self.current_display = str(eval(self.total_display))
            self.total_display = ""
            self.update_current_label()
        except Exception:
            self.current_display = "Error"
        finally:
            self.update_current_label()
            
        
    def setclear(self):
        self.current_display = ""
        self.total_display = ""
        self.update_current_label()
        self.update_total_label()
        
    def create_square(self):
        self.current_display = str(eval(f"{self.current_display}**2"))
        self.update_current_label()
        
    def create_sqrt(self):
        self.current_display = str(eval(f"{self.current_display}**0.5"))
        self.update_current_label()
        
        
    def create_special_button(self):
        button = Button(self.buttom_frame, text="=", bg="blue", fg="black", borderwidth=0, font=button_font, command=self.set_equal)
        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)
        
        clearB = Button(self.buttom_frame, text="C", bg="white", fg="black", borderwidth=0, font=button_font, command=self.setclear)
        clearB.grid(row=0, column=1, sticky=NSEW)
        
        square = Button(self.buttom_frame, text="x\u00b2", bg="white", fg="black", borderwidth=0, font=button_font, command=self.create_square)
        square.grid(row=0, column=2, sticky=NSEW)
        
        sqrt = Button(self.buttom_frame, text="\u221ax", bg="white", fg="black", borderwidth=0, font=button_font, command=self.create_sqrt)
        sqrt.grid(row=0, column=3, sticky=NSEW)
        
        
    def update_total_label(self):
        self.total_label.config(text=self.total_display)
        
    def update_current_label(self):
        self.current_label.config(text=self.current_display[:5])
        
    def bind_key(self):
        self.window.bind("<Return>", lambda event: self.set_equal())
        for key in self.digit:
            self.window.bind(str(key), lambda event, digit=key: self.expression(digit))
        for key in self.operators:
            self.window.bind(str(key), lambda event, operator=key: self.add_operator(operator))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.run()