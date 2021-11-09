from tkinter import ttk

import tkinter as tk

import sqlite3

import createCsvFromDb


def view():

    con1 = sqlite3.connect('chinook.db')

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM employees")

    rows = cur1.fetchall()

    for row in rows:

        tree.insert("", tk.END, values=row)

    con1.close()


# connect to the database
createCsvFromDb.main()

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="FNAME")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="LNAME")

tree.pack()

button1 = tk.Button(text="Display data", command=view)

button1.pack(pady=10)

root.mainloop()