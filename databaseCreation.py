import sqlite3 as sql
from os import path

class databaseCreation:

    def __init__(self):
        # creates a connection to the database included in the repository 
        # if it does not exist then it should create a new one
        self.databse_connection = sql.connect(f'{path.dirname(path.abspath(__file__))}/database1.db')
        self.cursor = self.databse_connection.cursor()

    def createTable(self, table_name, column_names = None, column_types = None):
        #creates table if there is at least one column name
        if(column_types == None or column_names == None or len(column_names) == 0 or len(column_types) == 0):
            return "Table Not Created: No column names or types."

        columnString = ""
        i = 0
        for column_name in column_names:
            if(len(column_types) - 1 == i):
                columnString = columnString + f"{column_name} {column_types[i]}"
            else:
                columnString = columnString + f"{column_name} {column_types[i]},"

            i += 1
        #sqlcommand
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columnString})")

        return "Table created successfully or table already exists."

    def removeItem(self, table_name, column_name, id):
        #removes a row from a table where id is found in specified column
        values = (id,)
        try:
            self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name}= ?", values)
            self.databse_connection.commit()
        except:
            return f"Could not remove {id} from table {table_name}. \nCheck column name and value."

        return f"Removed {id} from table {table_name}"

    def addItem(self, table_name, fields = None, types = None):
        #adds item to the table
        #enforces type
        fields = self.convert_values(fields, types)
        if(not fields):
            return "Was not able to add to table. \nCheck number of inputs and input type."
        try:
            values = []
            string1 = "("
            i = 0
            # ? are wildcards in sqlite and this creates a string to 
            # allow correct placement and number of wildcards in SQL command
            for field in fields:

                values.append(field)

                if (len(fields) -1 == i):
                    string1 = string1 + "?)"
                else:
                    string1 = string1 + "?,"
                
                i += 1
            self.cursor.execute(f"INSERT INTO {table_name} VALUES {string1}", values)
            self.databse_connection.commit()
        except:
            return "Was not able to add to table. \nCheck number of inputs and input type."

        return "Successfully Added to Table"

    def editItem(self, table_name, change_column, change, id, id_value):
        #edits rows where id_value is in id column
        values = (change, id_value)
        try:
            self.cursor.execute(f"UPDATE {table_name} SET {change_column}= ? WHERE {id}= ?", values)
            self.databse_connection.commit()
        except:
            return f"Failed to change {change_column} for {id_value} in table {table_name}.\n Check column names and values."
        return f"Successfully Updated {change_column} for {id_value} in table {table_name}"

    def displayTable(self, table_name):
        # displays all rows from a selected table
        try:
            column_num = self._get_num_columns(table_name)
            tableInString = ""
            data = self.cursor.execute(f"SELECT * FROM {table_name}")
            for column in data.description:
                tableInString  = tableInString + "{:>10} ".format(column[0])
            for record in self.cursor.fetchall():
                if(column_num == 1):
                    tableInString = tableInString + "\n{:>10} ".format(record[0])
                if(column_num == 2):
                    tableInString = tableInString + "\n{:>10} {:>10}".format(record[0], record[1])
                if(column_num == 3):
                    tableInString = tableInString + "\n{:>10} {:>10} {:>10}".format(record[0], record[1], record[2])
                if(column_num == 4):
                    tableInString = tableInString + "\n{:>10} {:>10} {:>10} {:>10}".format(record[0], record[1], record[2], record[3])
                if(column_num == 5):
                    tableInString = tableInString + "\n{:>10} {:>10} {:>10} {:>10} {:>10}".format(record[0], record[1], record[2], record[3], record[4])
        except:
            return "No table with that name found. \nTry creating it first."    
        return tableInString

    def displayItem(self, table_name, column_name, item):
        # display rows where column contains item
        try:
            column_num = self._get_num_columns(table_name)
            data = self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name}= '{item}'")
            tableInString = ""
            for column in data.description:
                tableInString = tableInString + "{:>10} ".format(column[0])
            for record in self.cursor.fetchall():
                if(column_num == 1):
                    tableInString = tableInString + "\n{:>10} ".format(record[0])
                if(column_num == 2):
                    tableInString = tableInString + "\n{:>10} {:>10}".format(record[0], record[1])
                if(column_num == 3):
                    tableInString = tableInString + "\n{:>10} {:>10} {:>10}".format(record[0], record[1], record[2])
                if(column_num == 4):
                    tableInString = tableInString + "\n{:>10} {:>10} {:>10} {:>10}".format(record[0], record[1], record[2], record[3])
                if(column_num == 5):
                    tableInString = tableInString + "\n{:>10} {:>10} {:>10} {:>10} {:>10}".format(record[0], record[1], record[2], record[3], record[4])
        except:
            return "No column matching that name check spelling."
        return tableInString

    def _get_num_columns(self, table_name):
        # returns the number of columns in a table
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            list1 = self.cursor.fetchall() 
            numCol = len(list1[0])
        except:
            return 0
        return numCol

    def convert_values(self, values, value_types):
        #attempts to convert values to column type 
        #if it falis will return 0
        i = 0
        for value in values:
            if value_types[i] == "INT":
                try:
                    values[i] = int(value)
                except:
                    return 0
            if value_types[i] == "TEXT":
                pass
            if value_types[i] == "REAL":
                try:
                    values[i] = float(value)
                except:
                    return 0
            if value_types[i] == "DATE":
                pass
            if value_types[i] == "BOOL":
                try:
                    values[i] = int(value)
                    if(values[i]):
                        values[i] = "TRUE"
                    else:
                        values[i] = "FALSE"
                except:
                    return 0
            i+=1
        return values

    def display_table_names(self):
        # displays all tables in database
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        
        i = 0
        string1 = ""
        for table in self.cursor.fetchall():
            string1 = string1 + f"\n{table}"
            i = 1
        
        if i == 0:
            return "No tables in database. Try creating one."

        return string1

    def delete_table(self, table_name):
        #deletes table from database
        try:
            self.cursor.execute(f"DROP TABLE {table_name}")
        except:
            return "Error Deleting Table. \nCheck If Table Exists."
        return f"Successfully Dropped Table: {table_name}"