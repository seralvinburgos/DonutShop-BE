import pymongo
import certifi

con_str = "mongodb+srv://seralvin:fsdi1234@cluster0.ppg4gsv.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("DonutShop")


me = {
    "first_name": "Alvin",
    "last_name": "Burgos",
    "age": 40
}

def hello():
    print("Hello there")