import sqlite3
from sqlite3 import Error


db_file = "/home/ubuntu/db/a2.db"
tableName = "onetab"
columnNames = { 'name': 'SMALLINT(3)',
                'age': 'SMALLINT(3)',
                'idno' : 'VARCHAR(32)'
              }

params = {"name":'raj',
          "age":21,
          "idno":"ddddddd"
        }

conn=None
c = None
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            #c.execute(create_table_sql)
            fieldset = []
            for col, definition in columnNames.items():
                fieldset.append("{0} {1}".format(col, definition))
            if len(fieldset) > 0:
                try:
                    query = "CREATE TABLE IF NOT EXISTS {0} ({1})".format(tableName, ", ".join(fieldset))
                    c.execute(query)
                    #c.commit()
                    return 0
                except sqlite3.Error as e:
                    print("ERROR:Unable to create table: " + tableName + " due to: " + str(e))
                    return 1

        except Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")



def writeData (params):
    create_table()
    conn = create_connection()
    if conn is not None:
        c = conn.cursor()
        try:
            rec = params
            keys = ','.join(rec.keys())
            question_marks = ','.join(list('?'*len(rec)))
            rowData = tuple(rec.values())
            c.execute('INSERT INTO '+tableName+' ('+keys+') VALUES ('+question_marks+')', rowData)
            conn.commit()
            close_connection()
            print("INFO: Successfully insert data into table: " + tableName + " data:" + str(params))
        except sqlite3.Error as e:
            print("ERROR: Unable to insert data into table: ",tableName +" due to: " + str(e))
            close_connection()
            return 2
        return 0

def read_Data():
    conn = create_connection()
    if conn is not None:
        c = conn.cursor()
        try:
            query = 'select * from ' + self.tableName
            c.execute(query)
            pts = [dict(row) for row in self.SQL.fetchall()]
            print("INFO: Successfully read data from table: " + tableName + " data:" + str(params))
            return pts 
        except sqlite3.Error as e:
            print("ERROR: Unable to read data from table: ",tableName +" due to: " + str(e))
            return 2
        return 0

def close_connection():
    try:
        conn.close()
        conn = None
        c = None
        print("DBG:successfully closed the connection for table: ",tableName )
    except:
        print("ERROR: Cannot close the conn.. for table: "+ str(tableName) + " due to: " )
    
create_table()
writeData(params)
