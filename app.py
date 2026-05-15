import datetime

def salam():
    indi=datetime.datetime.now()
    print(f"Salam! Hazirki vaxt: {indi}")
    print("Bu menim ilk Docker tetbiqimdir")

if __name__=="__main__":
    salam()

