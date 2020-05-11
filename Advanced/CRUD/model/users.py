from lib import conndb

def list_employees(self):
        db = conndb.Database()
        self.cur.execute("SELECT * FROM tbl_user LIMIT 50")
        result = self.cur.fetchall()
        return result