import sqlalchemy as sa

class MoneyStore:
    def __init__(self):
        self.url = 'mysql+mysqldb://root:PASSWORD@0.0.0.0:3306/line_bot?charset=utf8'
        self.engine = sa.create_engine(self.url, echo=True)

    def add_money(self, money):
        # データを抽出
        rows = self.engine.execute('SELECT * FROM money ORDER BY id DESC LIMIT 1')

        ins = "INSERT INTO money (timestamp, money) VALUES (%s, %s)"
        for row in rows:
            self.engine.execute(ins, money.get_tuple(row[2]))


        # 表示
        for row in rows:
            print(row)

    def get_money(self):
        sql = 'SELECT * FROM money ORDER BY id DESC LIMIT 1'
        return self.engine.execute(sql)
