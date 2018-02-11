# firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class MoneyStore:
    def __init__(self):
        # Fetch the service account key JSON file contents
        self.cred = credentials.Certificate('./linebot-9926a-firebase-adminsdk-uxbj1-35557599c8.json')

        # Initialize the app with a custom auth variable, limiting the server's access
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://linebot-9926a.firebaseio.com',
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })

        # The app only has access as defined in the Security Rules
        self.ref = db.reference('/another_resource')

        ## add data to database
        self.money_ref = self.ref.child('money')

    def add_money(self, money):
        self.money_ref.set({
            'mituba': {
                'timestamp': money.timestamp,
                'value': money.money
                }
            })

    def get_money(self):
        return int(self.ref.get()['money']['mituba']['value'])
