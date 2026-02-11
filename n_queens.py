import tkinter as tk
from tkinter import messagebox
import random

label_ids = [] 

class Info(tk.Label):
    def __init__(self, root1):
        tk.Label.__init__(self, root1)
        self.root1 = root1
        self.label = tk.Label(self, text='Welcome to N-Queens Puzzle!\nEnter a number N to define the board size and the number of queens.\nThe value must be an integer greater than 3.', fg='black', font=('Century', 24))
        self.label.pack(fill='both', expand=True)

class AskN(tk.Frame):
    def __init__(self, root1):
        tk.Frame.__init__(self, root1)
        self.root1 = root1
        self.label = tk.Label(self, text='Enter N:', fg='black', font=('Century', 24))
        self.label.pack(side='left', fill='both', expand=True)
        self.entry = tk.Entry(self, font=('Century', 24), fg='black')
        self.entry.pack(side='left', fill='both', expand=True)
        self.button = tk.Button(self, text='OK', fg='black', font=('Century', 24), command=self.buttonPushed)
        self.button.pack(side='left', fill='both', expand=True)

    def buttonPushed(self):
        global x, label_ids
        label_ids = [] 
        
        entry_val = self.entry.get()
        try:
            x = int(entry_val)
        except:
            messagebox.showerror('Invalid Input', 'Error: The input must be an integer!')
            return
        if (x <= 3):
            messagebox.showerror('Invalid Input', 'Error: The number must be higher than 3!')
            return
            
        forbidden_cols = set()
        forbidden_diagp = set()
        forbidden_diagn = set()
        num_of_queens = 0
        board = [[0] * x for _ in range(x)]
        
        fillRow(board, 0, num_of_queens, forbidden_cols, forbidden_diagp, forbidden_diagn, x)

        root = tk.Toplevel()
        root.title(f"{x} Queens Solution")
        Chessy(root)

        row_counter = -1
        for line in board:
            row_counter += 1
            col_counter = -1
            for val in line:
                col_counter += 1
                if val == 1:
                    index = (x * row_counter) + col_counter
                    current_label = label_ids[index]
                  
                    if current_label.cget("bg") == 'white':
                        d = tk.PhotoImage(file='queenwhite5.gif')
                        current_label.configure(image=d)
                        current_label.image = d
                    else:
                        e = tk.PhotoImage(file='queenblack3.gif')
                        current_label.configure(image=e)
                        current_label.image = e

class Chessy():
    def __init__(self, root):
        i = 0 
        self.root = root
        self.frame = tk.Frame(root, bg='brown', padx=2, pady=2)
        self.frame.pack(fill='both', expand=True)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
  
        while i < int(x):
            if i % 2 == 0:
                for k in range(0, int(x), 2):
                   
                    label_black = tk.Label(self.frame, bg='black', width=8, height=4, image=None)
                    label_black.grid(row=i, column=k, sticky='NSEW')
                    self.frame.columnconfigure(k, weight=1)
                    label_ids.append(label_black)
                    
                    if k < int(x) - 1:
                        label_white = tk.Label(self.frame, bg='white', width=8, height=4, image=None)
                        label_white.grid(row=i, column=k+1, sticky='NSEW')
                        self.frame.columnconfigure(k+1, weight=1)
                        label_ids.append(label_white)

            else: 
                for k in range(0, int(x), 2):                    
                    label_white = tk.Label(self.frame, bg='white', width=8, height=4, image=None)
                    label_white.grid(row=i, column=k, sticky='NSEW')
                    self.frame.columnconfigure(k, weight=1)
                    label_ids.append(label_white)
                    
                    if k < int(x) - 1:
                        label_black = tk.Label(self.frame, bg='black', width=8, height=4, image=None)
                        label_black.grid(row=i, column=k+1, sticky='NSEW')
                        self.frame.columnconfigure(k+1, weight=1)
                        label_ids.append(label_black)

            self.frame.grid_rowconfigure(i, weight=1)
            i += 1

def legal_pos(board, row, col, forbidden_cols, forbidden_diagp, forbidden_diagn):
    if col in forbidden_cols:
        return False
    if row + col in forbidden_diagp:
        return False
    if row - col in forbidden_diagn:
        return False
    return True

def fillRow(board, row, num_of_queens, forbidden_cols, forbidden_diagp, forbidden_diagn, x):
    if num_of_queens == x:
        return True
    if row == x:
        return False
    
    jj = list(range(0, x))
    random.shuffle(jj)   
    for j in jj:
        if legal_pos(board, row, j, forbidden_cols, forbidden_diagp, forbidden_diagn):
            board[row][j] = 1
            num_of_queens += 1
            forbidden_cols.add(j)
            forbidden_diagp.add(row + j)
            forbidden_diagn.add(row - j)
            if fillRow(board, row + 1, num_of_queens, forbidden_cols, forbidden_diagp, forbidden_diagn, x):
                return True
            else:
                board[row][j] = 0
                forbidden_cols.remove(j)
                forbidden_diagp.remove(row + j)
                forbidden_diagn.remove(row - j)
                num_of_queens -= 1
    return False

if __name__ == '__main__':
    root1 = tk.Tk()
    root1.title('ChessBoard')
    root1.geometry('1100x400')
    Info(root1).pack(fill='both', expand=True)
    AskN(root1).pack(side='left', fill='both', expand=True)
    root1.mainloop()