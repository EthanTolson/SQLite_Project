import tkinter as tk
from databaseCreation import databaseCreation as dc
class display():
    def __init__(self):
        # create tkinter object set the title and create a database creation object to work with the database
        self.window = tk.Tk()
        self.window.title("Database Creation")
        self.window.state('zoomed')
        self.window.geometry("500x500")
        self.data = dc()

    def drawInterface(self):
        # list of possible types a user can select when creating a table
        variableOptions = ["TEXT", "INT", "REAL", "DATE", "BOOL"]

        # these buttons controll the actions the user has
        self.button1 = tk.Button(text="Create Table", background="Green",activebackground="Red", font=2, width=15, height=2, command = self.createTable)
        self.button2 = tk.Button(text="Add to Table", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.addToTable)
        self.button3 = tk.Button(text="Display Table", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.displayTable)
        self.button4 = tk.Button(text="Get Item(s)\n From Table", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.getFromTable)
        self.button5 = tk.Button(text="Edit Item(s)\n From Table", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.editTable)
        self.button6 = tk.Button(text="Delete Item(s)\n From Table", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.deleteFromTable)
        self.button7 = tk.Button(text="Display All\n Table Names", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.displayAllTables)
        self.button8 = tk.Button(text="Delete Table", background="Green",activebackground="Red", font=2, width=15, height=2,command=self.delete_table)
        
        # these entrys allow the user to input table names and values to create tables and query
        #table name
        self.entry1 = tk.Entry()
        #column names
        self.entry2 = tk.Entry()
        self.entry3 = tk.Entry()
        self.entry4 = tk.Entry()
        self.entry5 = tk.Entry()
        self.entry6 = tk.Entry()
        # column values
        self.entry7 = tk.Entry()
        self.entry8 = tk.Entry()
        self.entry9 = tk.Entry()
        self.entry10 = tk.Entry()
        self.entry11 = tk.Entry()
        #edit column values and names
        self.entry12 = tk.Entry()
        self.entry13 = tk.Entry()
        self.entry14 = tk.Entry()
        self.entry15 = tk.Entry()
        #get tiem values and column names
        self.entry16 = tk.Entry()
        self.entry17 = tk.Entry()
        #del item value and column names
        self.entry18 = tk.Entry()
        self.entry19 = tk.Entry()


        #this lable is used as the output for any usercommnds and errors
        self.label1 = tk.Label()

        #labels to describe entry boxes
        self.label2 = tk.Label(text= "Table Name")
        self.label3 = tk.Label(text = "Column name")
        self.label4 = tk.Label(text = "Column Name")
        self.label5 = tk.Label(text = "Column Name")
        self.label6 = tk.Label(text = "Column Name")
        self.label7 = tk.Label(text = "Column Name")

        self.label8 = tk.Label(text = "Field 1")
        self.label9 = tk.Label(text = "Field 2")
        self.label10 = tk.Label(text = "Field 3")
        self.label11 = tk.Label(text = "Field 4")
        self.label12 = tk.Label(text = "Field 5")

        self.describe_add = tk.Label(text="Add: Fill out each box that has a title\n to add an item to the table.\nUse Display Table to show column names.")
        self.describe_add.grid(row = 3, rowspan= 2, column=1, padx=10, pady=10)

        self.describe_edit = tk.Label(text="Edit: Fill out each box \n to edit an item(s) in the table.\nExample: \nChange Pay To 1000 \nWhere Employee_ID Equals 3")
        self.describe_edit.grid(row = 5, rowspan= 2, column=1, padx=10, pady=10)

        self.label13 = tk.Label(text = "Change")
        self.label14 = tk.Label(text = "To")
        self.label15 = tk.Label(text = "Where")
        self.label16 = tk.Label(text = "Equals")

        self.describe_getitem = tk.Label(text="Get Item: Fill out each box \n to retrive an item(s) in the table.\nExample: \nDisplay Row(s) Where Pay Equals 1000")
        self.describe_getitem.grid(row = 7, rowspan= 2, column=1, padx=10, pady=10)
        self.label17 = tk.Label(text="Display Row(s) Where")
        self.label18 = tk.Label(text="Equals")

        self.describe_delitem = tk.Label(text="Delete Item: Fill out each box \n to delete an item(s) in the table.\nExample: \nDelete Row(s) Where Pay Equals 1000")
        self.describe_delitem.grid(row = 9, column=1, padx=10, pady=10)
        self.label19 = tk.Label(text="Delete Row(s) Where")
        self.label20 = tk.Label(text="Equals")
        
        #drop down menus for types
        self.clicked1 = tk.StringVar()
        self.clicked1.set("TEXT")
        self.dropDown1 = tk.OptionMenu(self.window, self.clicked1, *variableOptions)
        self.clicked2 = tk.StringVar()
        self.clicked2.set("TEXT")
        self.dropDown2 = tk.OptionMenu(self.window, self.clicked2, *variableOptions)
        self.clicked3 = tk.StringVar()
        self.clicked3.set("TEXT")
        self.dropDown3 = tk.OptionMenu(self.window, self.clicked3, *variableOptions)
        self.clicked4 = tk.StringVar()
        self.clicked4.set("TEXT")
        self.dropDown4 = tk.OptionMenu(self.window, self.clicked4, *variableOptions)
        self.clicked5 = tk.StringVar()
        self.clicked5.set("TEXT")
        self.dropDown5 = tk.OptionMenu(self.window, self.clicked5, *variableOptions)

        #placing all buttons, entries, and dropdown menus onto the window
        self.entry1.grid(row=1, column=1, padx=10, pady=10)
        self.entry2.grid(row=1, column=2, padx=10, pady=10)
        self.entry3.grid(row=1, column=3, padx=10, pady=10)
        self.entry4.grid(row=1, column=4, padx=10, pady=10)
        self.entry5.grid(row=1, column=5, padx=10, pady=10)
        self.entry6.grid(row=1, column=6, padx=10, pady=10)

        self.entry7.grid(row=4, column=2, padx=10, pady=10)
        self.entry8.grid(row=4, column=3, padx=10, pady=10)
        self.entry9.grid(row=4, column=4, padx=10, pady=10)
        self.entry10.grid(row=4, column=5, padx=10, pady=10)
        self.entry11.grid(row=4, column=6, padx=10, pady=10)

        self.entry12.grid(row=5, column=3, padx=10, pady=10)
        self.entry13.grid(row=5, column=5, padx=10, pady=10)
        self.entry14.grid(row=6, column=3, padx=10, pady=10)
        self.entry15.grid(row=6, column=5, padx=10, pady=10)

        self.entry16.grid(row=7, column=3, padx=10, pady=10)
        self.entry17.grid(row=7, column=5, padx=10, pady=10)

        self.entry18.grid(row=9, column=3, padx=10, pady=10)
        self.entry19.grid(row=9, column=5, padx=10, pady=10)

        self.dropDown1.grid(row=2, column=2, padx=10, pady=10)
        self.dropDown2.grid(row=2, column=3, padx=10, pady=10)
        self.dropDown3.grid(row=2, column=4, padx=10, pady=10)
        self.dropDown4.grid(row=2, column=5, padx=10, pady=10)
        self.dropDown5.grid(row=2, column=6, padx=10, pady=10)

        self.button1.grid(row=0,column=0, padx=10, pady=10)
        self.button2.grid(row=1, column=0, padx=10, pady=10)
        self.button3.grid(row=2, column=0, padx=10, pady=10)
        self.button4.grid(row=3, column=0, padx=10, pady=10)
        self.button5.grid(row=4, column=0, padx=10, pady=10)
        self.button6.grid(row=5, column=0, padx=10, pady=10)
        self.button7.grid(row=6, column=0, padx=10, pady=10)
        self.button8.grid(row=7, column=0, padx=10, pady=10)

        self.label2.grid(row=0,column=1,padx=10, pady=10)
        self.label3.grid(row=0,column=2,padx=10, pady=10)
        self.label4.grid(row=0,column=3,padx=10, pady=10)
        self.label5.grid(row=0,column=4,padx=10, pady=10)
        self.label6.grid(row=0,column=5,padx=10, pady=10)
        self.label7.grid(row=0,column=6,padx=10, pady=10)

        self.label8.grid(row=3,column=2,padx=10, pady=10)
        self.label9.grid(row=3,column=3,padx=10, pady=10)
        self.label10.grid(row=3,column=4,padx=10, pady=10)
        self.label11.grid(row=3,column=5,padx=10, pady=10)
        self.label12.grid(row=3,column=6,padx=10, pady=10)

        self.label13.grid(row=5,column=2,padx=10, pady=10)
        self.label14.grid(row=5,column=4,padx=10, pady=10)
        self.label15.grid(row=6,column=2,padx=10, pady=10)
        self.label16.grid(row=6,column=4,padx=10, pady=10)

        self.label17.grid(row=7,column=2,padx=10, pady=10)
        self.label18.grid(row=7,column=4,padx=10, pady=10)

        self.label19.grid(row=9,column=2,padx=10, pady=10)
        self.label20.grid(row=9,column=4,padx=10, pady=10)
    
    def checkTableName(self):
        if(len(self.entry1.get()) <= 0):
            self.label1.destroy()
            self.label1 = tk.Label(text = "Please Enter Table Name.")
            self.label1.grid(row=0, rowspan=8, column=7, padx=10, pady=10)
            return False
        return True

    def createTable(self):
        #creates table 
        if(not self.checkTableName()):
            return

        column_names = []
        column_types = []

        if(len(self.entry2.get())): 
            column_names.append(self.entry2.get())
            column_types.append(self.clicked1.get())
        
        if(len(self.entry3.get())): 
            column_names.append(self.entry3.get())
            column_types.append(self.clicked2.get())

        if(len(self.entry4.get())): 
            column_names.append(self.entry4.get())
            column_types.append(self.clicked3.get())

        if(len(self.entry5.get())): 
            column_names.append(self.entry5.get())
            column_types.append(self.clicked4.get())

        if(len(self.entry6.get())): 
            column_names.append(self.entry6.get())
            column_types.append(self.clicked5.get())

        self.label1.destroy()
        self.label1 = tk.Label(text = self.data.createTable(self.entry1.get(), column_names, column_types))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)
        

    def addToTable(self):
        if(not self.checkTableName()):
            return

        values = []
        value_types = []

        if(len(self.entry7.get())): 
            values.append(self.entry7.get())
            value_types.append(self.clicked1.get())
        
        if(len(self.entry8.get())): 
            values.append(self.entry8.get())
            value_types.append(self.clicked2.get())

        if(len(self.entry9.get())): 
            values.append(self.entry9.get())
            value_types.append(self.clicked3.get())

        if(len(self.entry10.get())): 
            values.append(self.entry10.get())
            value_types.append(self.clicked4.get())

        if(len(self.entry11.get())): 
            values.append(self.entry11.get())
            value_types.append(self.clicked5.get())

        
        self.label1.destroy()
        self.label1 = tk.Label(text = self.data.addItem(self.entry1.get(), values, value_types))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)

    def displayTable(self):
        if(not self.checkTableName()):
            return

        try:
            self.label8.destroy()
            self.label9.destroy()
            self.label10.destroy()
            self.label11.destroy()
            self.label12.destroy()

            data = self.data.cursor.execute(f"SELECT * FROM {self.entry1.get()}")
            i = 0
            for column in data.description:
                if(i == 0):
                    self.label8.destroy()
                    self.label8  = tk.Label(text="{:>10} ".format(column[0]))
                    self.label8.grid(row=3,column=2,padx=10, pady=10)
                    self.entry7.destroy()
                    self.entry7 = tk.Entry()
                    self.entry7.grid(row=4, column=2, padx=10, pady=10)
                if(i == 1):
                    self.label9.destroy()
                    self.label9  = tk.Label(text="{:>10} ".format(column[0]))
                    self.label9.grid(row=3,column=3,padx=10, pady=10)
                    self.entry8.destroy()
                    self.entry8 = tk.Entry()
                    self.entry8.grid(row=4, column=3, padx=10, pady=10)
                if(i == 2):
                    self.label10.destroy()
                    self.label10  = tk.Label(text="{:>10} ".format(column[0]))
                    self.label10.grid(row=3,column=4,padx=10, pady=10)
                    self.entry9.destroy()
                    self.entry9 = tk.Entry()
                    self.entry9.grid(row=4, column=4, padx=10, pady=10)
                if(i == 3):
                    self.label11.destroy()
                    self.label11  = tk.Label(text="{:>10} ".format(column[0]))
                    self.label11.grid(row=3,column=5,padx=10, pady=10)
                    self.entry10.destroy()
                    self.entry10 = tk.Entry()
                    self.entry10.grid(row=4, column=5, padx=10, pady=10)
                if(i == 4):
                    self.label12.destroy()
                    self.label12  = tk.Label(text="{:>10} ".format(column[0]))
                    self.label12.grid(row=3,column=6,padx=10, pady=10)

                    self.entry11.destroy()
                    self.entry11 = tk.Entry()
                    self.entry11.grid(row=4, column=6, padx=10, pady=10)
                
                i+=1
        except:
            self.label1.destroy()
            self.label1 = tk.Label(text = "Please Enter Valid Table Name.")
            self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)
            return

        self.label1.destroy()
        self.label1 = tk.Label(text=self.data.displayTable(self.entry1.get()))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)

    def displayAllTables(self):
        self.label1.destroy()
        self.label1 = tk.Label(text=self.data.display_table_names())
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)
        return

    def delete_table(self):
        if(not self.checkTableName()):
            return
        self.label1.destroy()
        self.label1 = tk.Label(text=self.data.delete_table(self.entry1.get()))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)

    def getFromTable(self):
        if(not self.checkTableName()):
            return
        self.label1.destroy()
        self.label1 = tk.Label(text=self.data.displayItem(self.entry1.get(), self.entry16.get(), self.entry17.get()))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)
        pass

    def editTable(self):
        if(not self.checkTableName()):
            return
        self.label1.destroy()
        self.label1 = tk.Label(text=self.data.editItem(self.entry1.get(),self.entry12.get(), self.entry13.get(), self.entry14.get(), self.entry15.get()))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)

    def deleteFromTable(self):
        if(not self.checkTableName()):
            return
        self.label1.destroy()
        self.label1 = tk.Label(text=self.data.removeItem(self.entry1.get(), self.entry18.get(), self.entry19.get()))
        self.label1.grid(row=0,rowspan=8,column=7,padx=10, pady=10)