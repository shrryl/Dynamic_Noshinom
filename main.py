from libdw import pyrebase

dburl = "https://ieee-ntu-default-rtdb.asia-southeast1.firebasedatabase.app"
email = "hello@test.com"
password = "hello123"
apikey = "AIzaSyBFyMmjF4SQIGQeI4c3cbh5TwvPYdEgGfs"
authdomain = dburl.replace("https://ieee-ntu-default-rtdb.asia-southeast1.firebasedatabase.app","hello")


config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken'])
chicken_ref = db.child('Chicken')

def main():
    while True:
        choice = input("1 - Upload a new price. 2 - Change price for an existing day.") 
        if choice == 1:
            uploadPrice()
        elif choice == 2:
            changePrice()
        else:
            print("Please enter a valid option.")
            

def uploadPrice():
    print("Upload chicken date and price")
    value = str(input("Enter date DDMMYY: "))
    value1 = input("Enter price: ")
    db.child(value).set({"price": value1})

    print("please go to the firebase console and have a look")


def changePrice():
    changeval = input("Enter Date DDMMYY: ")
    print(db.child('Chicken').order_by_key())

    if changeval in db.child("Chicken").get():
        print(changeval)
   # node = db.child('Chicken').get(changeval)

changePrice()