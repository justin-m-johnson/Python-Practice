def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#main() <--- DONT CALL MAIN
    
if __name__ == "__main__": #this is if I run sayings.py alone!
    main()