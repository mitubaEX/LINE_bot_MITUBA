import sqlalchemy as sa

class UsersStore:
    def __init__(self):
        self.url = 'mysql+mysqldb://root:PASSWORD@0.0.0.0:3306/line_bot?charset=utf8'
        self.engine = sa.create_engine(self.url, echo=True)

    def add_user(self, user):
        ins = "INSERT INTO users (display_name, user_id, picture_url, status_message) VALUES (%s, %s, %s, %s)"
        self.engine.execute(ins, user.get_tuple())

        # データを抽出
        rows = self.engine.execute('SELECT * FROM users')

        # 表示
        for row in rows:
            print(row)

    def get_users(self):
        sql = "SELECT user_id FROM users"
        return self.engine.execute(sql)
