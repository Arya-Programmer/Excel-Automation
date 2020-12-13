import sqlite3 as db


class Excel:
    def __init__(self):
        self.conn = db.connect("Fields.db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS WORK(
            title text NOT NULL UNIQUE, 
            type text,
            file_location text,
            worksheet_name text,
            first_column text,
            field_number integer
        )""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS FIELDS(
            work_title text,
            name text, 
            type text,
            option text,
            formula text
        )""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS HISTORY(
            work_title text,
            name text,    
            option text
        )""")

        self.conn.commit()
        self.conn.close()

    def addWork(self, fields, work):
        for name, option, type, formula in fields:
            self.insertField(work[0], name, option, type, formula)

        # ['Hello', 'C:/Users/1234/Desktop', 1, 'Month Name', 'Date', 'Excel']
        self.insertWork(work[0], work[-1], work[1], work[3], work[4], work[2])

    def insertField(self, title, name, option, type, formula):
        self.connectToDB()
        self.c.execute("INSERT INTO FIELDS VALUES (:title, :name, :type, :option, :formula)", {
            'title': str(title),
            'name': str(name),
            'type': str(type),
            'option': str(option),
            'formula': str(formula),
        })
        self.conn.commit()
        self.conn.close()

    def insertWork(self, title, type, file_location, worksheet, firstCol, fieldNum):
        self.connectToDB()
        self.c.execute(
            "INSERT INTO WORK VALUES (:title, :type, :file_location, :worksheet_name, :first_column, :field_number)", {
                'title': str(title),
                'type': str(type),
                'file_location': str(file_location),
                'worksheet_name': str(worksheet),
                'first_column': str(firstCol),
                'field_number': int(fieldNum),
            })
        self.conn.commit()
        self.conn.close()

    def insertHistory(self, title, name, option):
        self.connectToDB()
        self.c.execute("INSERT INTO HISTORY VALUES (:title, :name, :option)", {
            'title': str(title),
            'name': str(name),
            'option': str(option),
        })
        self.conn.commit()
        self.conn.close()

    def getLastInputOf(self, table):
        self.connectToDB()
        self.c.execute(f"SELECT oid, * FROM {table} ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.conn.close()
        return result

    def getAll(self, table):
        self.connectToDB()
        self.c.execute(f"SELECT oid, * FROM {table}")
        result = self.c.fetchall()
        self.conn.close()
        return result

    def getId(self, table):
        self.connectToDB()
        self.c.execute(f"SELECT oid FROM {table}")
        result = self.c.fetchall()
        self.conn.close()
        return result

    def getAllById(self, table, id):
        self.connectToDB()
        self.c.execute(f"SELECT oid, * FROM {table} WHERE oid={id}")
        result = self.c.fetchall()
        self.conn.close()
        return result

    def getAllByTitle(self, table, title):
        self.connectToDB()
        self.c.execute(f"SELECT oid, * FROM {table} WHERE work_title='{title}'")
        result = self.c.fetchall()
        self.conn.close()
        return result

    def getTheLast(self, num, table, whereTitleIs):
        self.connectToDB()
        self.c.execute(
            f"SELECT * FROM (SELECT oid, * FROM {table} WHERE work_title='{whereTitleIs}' ORDER BY oid DESC LIMIT {num}) ORDER BY oid ASC")
        result = self.c.fetchall()
        self.conn.close()
        return result

    def connectToDB(self):
        self.conn = db.connect("Fields.db")
        self.c = self.conn.cursor()
