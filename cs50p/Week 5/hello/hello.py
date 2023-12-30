def main():
    name = input("What is your name?")
#    hello(name)
    print(hello(name))

#As this sits right now, it doesn't return and it isn't testable...  "Don't test side effects"
'''
def hello(to="world"):
    print("hello,", to)
'''
def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()