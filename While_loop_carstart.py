x = str(input())
while x == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
    if str(input()) == "start":
        print("car started...Ready to go!")
    if str(input()) == "stop":
        print("car stopped")
    if str(input()) == "quit":
        break
else:
    print("I don't understand that...")