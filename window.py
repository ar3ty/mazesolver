from tkinter import Tk, BOTH, Canvas, ttk, Toplevel
import re
from maze import Maze

class Window:
    def __init__(self):
        self.input = {
            "Margin" : "50",
            "Number of columns" : "10",
            "Number of rows" : "10",
            "Cell width" : "50",
            "Cell height" : "50",
        }
        self.__root = Tk()
        self.__root.title("mazesolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.__close)
        self.__is_solved = False
        self._is_closing = False
        self.__assign_values_window()

##maze_and_algorithm
    
    def __reinit(self):
        for widget in self.__root.winfo_children():
            widget.destroy()
        height = 2 * self.input["Margin"] + self.input["Number of rows"] * self.input["Cell height"]
        width = 2 * self.input["Margin"] + self.input["Number of columns"] * self.input["Cell width"]
        self.__root.geometry(f"{width}x{height}")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.algorithm = None
        self.maze = Maze(self.input['Margin'],
                self.input['Margin'], 
                self.input['Number of columns'], 
                self.input['Number of rows'], 
                self.input['Cell width'], 
                self.input['Cell height'],
                self)
        self.__choose_algorithm()

    def __solve_maze(self):
        if self.__is_solved == True:
            self.__canvas.delete("path")
        self.algo = self.combobox.get()
        self.__is_solved = self.maze.solve(self.algo)
        if self.__is_solved == False:
            label1 = ttk.Label(self.__new_win, text="Maze is not solved", foreground="red")
            label1.grid(row=6, column=0, ipadx=2, ipady=2, padx=2, pady=2)

    def __rebuild(self):
        self.__new_win.destroy()
        for widget in self.__root.winfo_children():
            widget.destroy()
        self.__assign_values_window()

    def __choose_algorithm(self):
        self.__new_win = Toplevel()
        self.__new_win.title("Algorithm")
        self.__new_win.protocol("WM_DELETE_WINDOW", self.__close)
        self.__new_win.geometry("200x150")
        algos = ["Breadth-First-Search",
                 "Depth-First-Search",
                 "A *"]

        self.combobox = ttk.Combobox(self.__new_win, values=algos)
        self.combobox.current(1)
        label = ttk.Label(self.__new_win, text="Choose search algorithm")
        label.grid(row=0, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.btn = ttk.Button(self.__new_win, text="Solve maze", command=self.__solve_maze)
        self.btn.grid(row=4, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.btn2 = ttk.Button(self.__new_win, text="Rebuild", command=self.__rebuild)
        self.btn2.grid(row=5, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.combobox.grid(row=1, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.__new_win.focus_force()
    
##initial_logic

    def __close(self):
        if hasattr(self, "__new_win"):
            self.__new_win.destroy()
        self._is_closing = True
        self.__root.after(100, self.__exit)
        
    def __exit(self):
        self.__root.destroy()
        exit(0)

    def draw_line(self, line, fill_color="black", is_path=False):
        if self._is_closing:
            return
        line.draw(self.__canvas, fill_color, is_path)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__root.mainloop()

##config_window

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
                if self.input[key] < 1: 
                    return self.throw_error()
        
        if (self.input["Number of columns"] * self.input["Cell width"] > 1024 
            or self.input["Number of rows"] * self.input["Cell height"] > 1024 
            or self.input["Margin"] > 100 
            or self.input["Number of columns"] * self.input["Number of rows"] > 1024):
            return self.throw_error()

        self.__reinit()

    def __assign_values_window(self):
        for widget in self.__root.winfo_children():
            widget.destroy()
        self.__root.geometry("200x250")
        self.__root.resizable(0, 0)
        self.label0 = ttk.Label(self.__root, text="Insert maze properties", font=("Helvetica", 10, "bold"))
        self.label0.grid(row=0, column=0, columnspan=2, ipadx=2, ipady=6, padx=2, pady=2)

        self.label1 = ttk.Label(self.__root, text="Margin")
        self.label1.grid(row=1, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry1 = ttk.Entry(self.__root, width=5)
        self.entry1.insert(0, self.input["Margin"])
        self.entry1.grid(row=1, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label2 = ttk.Label(self.__root, text="Number of columns")
        self.label2.grid(row=2, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry2 = ttk.Entry(self.__root, width=5)
        self.entry2.insert(0, self.input["Number of columns"])
        self.entry2.grid(row=2, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label3 = ttk.Label(self.__root, text="Number of rows")
        self.label3.grid(row=3, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry3 = ttk.Entry(self.__root, width=5)
        self.entry3.insert(0, self.input["Number of rows"])
        self.entry3.grid(row=3, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label4 = ttk.Label(self.__root, text="Cell width")
        self.label4.grid(row=4, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry4 = ttk.Entry(self.__root, width=5)
        self.entry4.insert(0, self.input["Cell width"])
        self.entry4.grid(row=4, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.label5 = ttk.Label(self.__root, text="Cell height")
        self.label5.grid(row=5, column=0, ipadx=2, ipady=2, padx=2, pady=2)
        self.entry5 = ttk.Entry(self.__root, width=5)
        self.entry5.insert(0, self.input["Cell height"])
        self.entry5.grid(row=5, column=1, ipadx=2, ipady=2, padx=2, pady=2)

        self.btn = ttk.Button(self.__root, text="Build maze", command=self.check_n_apply_entries)
        self.btn.grid(row=6, column=0, columnspan=2, ipadx=6, ipady=6, padx=4, pady=4)