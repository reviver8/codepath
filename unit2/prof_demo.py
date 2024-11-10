def hello():
    print("hello")

def intro():
    greetings = ["hi", "heya", "morning"]
    print(greetings[2])
    print("How many greetings? ", len(greetings))

def saySomething():
    print(4 + int("3"))
    hello()
    intro()

saySomething()