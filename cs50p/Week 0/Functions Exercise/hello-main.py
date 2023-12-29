def main():
    name = input("What is your name? ")
    hello(name)
    hello()

def hello(to="world"):
    print("Hello, ", to)

main()
#Added Main Function