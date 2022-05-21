# Overview


For the past two weeks I have been learning how to use SQL commands in python using the SQLite library. 
I learned SQL through MySQLWorkbench and wanted to learn how to exzecute SQL commands in Python.

I wrote a program that allows someone who does not know SQL to create, edit, add to, and drop tables in a database. 
My program starts a window using TKinter and has intructions on how to use it built in.
You simply enter data into the various entry fields and press buttons to execute commands.

I wanted to challenge myself by combining two concepts that I have learned as well as learning about Tkinter as a GUI building tool.
I also wanted to create something similar to MySQL workbench that allows someone who has no knowledge of SQL to interact with a database.

[Software Demo Video](https://youtu.be/DzwGIBX9Elo)

# Relational Database

I am using an SQLite database and am editing it using SQLite3 and Python. The database is empty as my program allows users to create tables and add values to those tables.
There should be no tables in the database for the reason listed above. My progrm allows users to create unconnected tables with up to 5 columns. They can choose the column names and types and enter whatever data they want.

# Development Environment

IDE: Visual Studio Code

Language: Python

Libraries: SQLlite, tkinter

# Useful Websites

* [TKinter Help](https://riptutorial.com/tkinter)
* [SQLite Documentation](https://www.sqlite.org/docs.html)
* [SQLite3 for Python Docs](https://docs.python.org/3/library/sqlite3.html)

# Future Work

* Fix the change item function to force types as SQLite does not do this automatically
* Add ability to join tables
