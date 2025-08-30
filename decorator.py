def greet(x):
    def mx():
        print("GM")
        x()
        print("thanks")
    return mx

@greet()
def wish():
    print("Have a nice day!")
wish()
