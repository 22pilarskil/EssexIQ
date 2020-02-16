import pyrebase

config = {
    "apiKey": "AIzaSyCJhmjij4ABEZrlIP5581ERp9pXcb6anLk",
    "authDomain": "n-d3a20.firebaseapp.com",
    "databaseURL": "https://n-d3a20.firebaseio.com",
    "projectId": "n-d3a20",
    "storageBucket": "n-d3a20.appspot.com",
    "messagingSenderId": "626961674461",
    "appId": "1:626961674461:web:424708683547daae",
    "serviceAccount": "static/n-d3a20-firebase-adminsdk-4gvqc-7e0b540d4f.json"
}

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("liampilarski2@gmail.com", "Liamlukas=11")
user = auth.refresh(user['refreshToken'])
db = firebase.database()
