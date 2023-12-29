def main():
    x = int(input("What is x? "))
    if is_even(x): #this passes "x" to the function "is_even" below
        print("Even")
    else:
        print("Odd")

def is_even(n): #this takes "x" and changes it to "n", runs it through the modulus, then if true, prints Even. If its false, it will essentially skip over to the "else" above
    if n % 2 == 0:
        return True
    else:
        return False
#Can rewrite this to: "return True if n % 2 == 0 else False" if we want to one line this
main()