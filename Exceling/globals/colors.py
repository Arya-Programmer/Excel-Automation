import sqlite3 as db


class ColorsBackend:
    def __init__(self):
        self.connect()
        noTable = False
        tablesDontExist = len(self.c.execute("SELECT name FROM sqlite_master").fetchall()) < 1
        if tablesDontExist:
            noTable=True
        self.c.execute("CREATE TABLE IF NOT EXISTS window(background TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS labels(text TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS buttons(background TEXT, text TEXT, hover TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS inputfield(background TEXT, text TEXT, focused TEXT, line TEXT, hover TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS tabs(background TEXT, text TEXT, focused TEXT, hover TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS cards(background TEXT, text TEXT, hover TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS dialogboxes(bg1 TEXT, bg2 TEXT, t1 TEXT, t2 TEXT, hover1 TEXT, hover2 TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS sidebar(bg TEXT, text TEXT, focused TEXT, hover TEXT)")
        if noTable:
            self.initialize()
        self.disconnect()

    def initialize(self):
        self.insertIntoWindow()
        self.insertIntoCards()
        self.insertIntoTabs()
        self.insertIntoLabels()
        self.insertIntoButtons()
        self.insertIntoSidebar()
        self.insertIntoInputfields()
        self.insertIntoDialogboxes()
    # noinspection PyAttributeOutsideInit
    def connect(self):
        self.conn = db.connect("Colors.db")
        self.c = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def insertIntoWindow(self, background="grey"):
        self.connect()
        self.c.execute(f"INSERT INTO window VALUES('{background}')")
        self.conn.commit()
        self.disconnect()

    def window(self):
        self.connect()
        self.c.execute("SELECT * FROM window ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.disconnect()
        return result

    def insertIntoLabels(self, text="#e4e6e8"):
        self.connect()
        self.c.execute(f"INSERT INTO labels VALUES('{text}')")
        self.conn.commit()
        self.disconnect()

    def labels(self):
        self.connect()
        self.c.execute("SELECT * FROM labels ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.disconnect()
        return result

    def insertIntoButtons(self, background="#141518", text="#e4e6e8", hover="#45474d"):
        self.connect()
        self.c.execute(f"INSERT INTO buttons VALUES('{background}', '{text}', '{hover}')")
        self.conn.commit()
        self.disconnect()

    def buttons(self):
        self.connect()
        self.c.execute("SELECT * FROM buttons ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.disconnect()
        return result

    def insertIntoInputfields(self, background="#e4e6e8", text="#141518", focused="#2c56d4", line="#141518", hover="#2c56d4"):
        self.connect()
        self.c.execute(f"INSERT INTO inputfield VALUES('{background}', '{text}', '{focused}', '{line}', '{hover}')")
        self.conn.commit()
        self.disconnect()

    def inputfields(self):
        self.connect()
        self.c.execute("SELECT * FROM inputfield ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.disconnect()
        return result

    def insertIntoTabs(self, background="#e4e6e8", text="white", focused="#141518", hover="#45474d"):
        self.connect()
        self.c.execute(f"INSERT INTO tabs VALUES('{background}', '{text}', '{focused}', '{hover}')")
        self.conn.commit()
        self.disconnect()

    def tabs(self):
        self.connect()
        self.c.execute("SELECT * FROM tabs ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.disconnect()
        return result

    def insertIntoDialogboxes(self, bg1="#436CA6", bg2="#2A292E", t1="#e4e6e8", t2="#e4e6e8", h1="#436CA6", h2="#2A292E"):
        self.connect()
        self.c.execute(f"INSERT INTO dialogboxes VALUES('{bg1}', '{bg2}', '{t1}', '{t2}', '{h1}', '{h2}')")
        self.conn.commit()
        self.disconnect()

    def dialogboxes(self):
        self.connect()
        self.c.execute("SELECT * FROM dialogboxes ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.disconnect()
        return result

    def insertIntoSidebar(self, bg="#e4e6e8", text="white", focused="#141518", hover="grey"):
        self.connect()
        self.c.execute(f"INSERT INTO sidebar VALUES('{bg}', '{text}', '{focused}', '{hover}')")
        self.conn.commit()
        self.disconnect()

    def sidebar(self):
        self.connect()
        self.c.execute(f"SELECT * FROM sidebar ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.conn.commit()
        self.disconnect()
        return result

    def insertIntoCards(self, bg="rgb(8, 8, 8)", text="white", hover="black"):
        self.connect()
        self.c.execute(f"INSERT INTO cards VALUES('{bg}', '{text}', '{hover}')")
        self.conn.commit()
        self.disconnect()

    def cards(self):
        self.connect()
        self.c.execute(f"SELECT * FROM cards ORDER BY oid DESC LIMIT 1")
        result = self.c.fetchone()
        self.conn.commit()
        self.disconnect()
        return result
