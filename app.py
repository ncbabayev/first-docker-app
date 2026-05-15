import datetime

def greet():
    now = datetime.datetime.now()
    print(f"Hello! Current time: {now}")
    print("This is my first Docker application!")

if __name__ == "__main__":
    greet()