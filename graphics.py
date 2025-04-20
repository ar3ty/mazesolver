from tkinter import Tk, BOTH, Canvas, ttk
import re

class Window:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("mazesolver")
        self.__running = False
        self.input = {
            "Margin" : None,
            "Number of columns" : None,
            "Number of rows" : None,
            "Cell width" : None,
            "Cell height" : None,
        }
        self.values_are_assigned = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__assign_values_window()

    
    def reinit(self):
        self.__root.destroy()
        self.__root = Tk()
        self.__root.title("mazesolver")
        height = 2 * self.input["Margin"] + self.input["Number of rows"] * self.input["Cell width"]
        width = 2 * self.input["Margin"] + self.input["Number of columns"] * self.input["Cell height"]
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.values_are_assigned = False
        self.algorithm = None
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__choose_algorithm()

    def __choose_algorithm(self):
        new_win = Tk()
        new_win.title("Algorithm")
        new_win.geometry("300x150")
        algos = ["Breadth-First-Search",
                 "Depth-First-Search",
                 "NonAvailable"]
        combobox = ttk.Combobox(new_win, textvariable=algos[0], values=algos)
        label = ttk.Label(new_win, text="Choose search algorithm")
        label.grid(row=0, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.btn = ttk.Button(new_win, text="Solve maze")
        self.btn.grid(row=0, column=1, ipadx=2, ipady=2, padx=2, pady=2)
        combobox.grid(row=1, column=0, columnspan=2, ipadx=2, ipady=2, padx=2, pady=2)


    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running and not self.values_are_assigned: 
            self.redraw()
        self.reinit()

    def close(self):
        self.__running = False

    def throw_error(self):
            label6 = ttk.Label(self.__root, text="Validate your entry values", foreground="red")
            label6.grid(row=7, column=0, columnspan=2, ipadx=2, ipady=2, padx=2, pady=2)

        
    def check_n_apply_entries(self):
        self.input["Margin"] = self.entry1.get()
        self.input["Number of columns"] = self.entry2.get()
        self.input["Number of rows"] = self.entry3.get()
        self.input["Cell width"] = self.entry4.get()
        self.input["Cell height"] = self.entry5.get()

        for key in self.input.keys():
            if self.input[key] == None or re.fullmatch(r'^\d+$', self.input[key])==None:
                return self.throw_error()
            else:
                self.input[key] = int(self.input[key])

        self.values_are_assigned = True

    def __assign_values_window(self):
        self.__root.geometry("200x250")
        self.__root.resizable(0, 0)
        self.label0 = ttk.Label(self.__root, text="Insert maze properties", font=("Helvetica", 10, "bold"))
        self.label0.grid(row=0, column=0, columnspan=2, ipadx=2, ipady=6, padx=2, pady=2)

        self.label1 = ttk.Label(self.__root, text="Margin")
        self.label1.grid(row=1, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry1 = ttk.Entry(self.__root, width=5)
        self.entry1.insert(0, "50")
        self.entry1.grid(row=1, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label2 = ttk.Label(self.__root, text="Number of columns")
        self.label2.grid(row=2, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry2 = ttk.Entry(self.__root, width=5)
        self.entry2.insert(0, "10")
        self.entry2.grid(row=2, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label3 = ttk.Label(self.__root, text="Number of rows")
        self.label3.grid(row=3, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry3 = ttk.Entry(self.__root, width=5)
        self.entry3.insert(0, "10")
        self.entry3.grid(row=3, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label4 = ttk.Label(self.__root, text="Cell width")
        self.label4.grid(row=4, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry4 = ttk.Entry(self.__root, width=5)
        self.entry4.insert(0, "50")
        self.entry4.grid(row=4, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label5 = ttk.Label(self.__root, text="Cell height")
        self.label5.grid(row=5, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry5 = ttk.Entry(self.__root, width=5)
        self.entry5.insert(0, "50")
        self.entry5.grid(row=5, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.btn = ttk.Button(self.__root, text="Build maze", command=self.check_n_apply_entries)
        self.btn.grid(row=6, column=0, columnspan=2, ipadx=6, ipady=6, padx=4, pady=4)
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)