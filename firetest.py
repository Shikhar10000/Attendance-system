import pyrebase
config = {'apiKey': 'AIzaSyAPZpriTOWoRQ4jTSTxf6jSdo-WQ6JSZXw', 'authDomain': 'testattendance-c9844.firebaseapp.com', 'databaseURL': 'https://testattendance-c9844.firebaseio.com','storageBucket': 'testattendance-c9844.appspot.com'}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("1234@abcd.com", "123456")
user['idToken']
db = firebase.database()

archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
db.child("agents").push(archer, user['idToken'])

lana = {"name": "Lana Kane", "agency": "Figgis Agency"}
db.child("agents").child("Lana").set(lana, user['idToken'])
