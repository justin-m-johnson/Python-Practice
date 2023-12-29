''' Original Code Below

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        #print(i, end=" ") # This is debugging the code - We see here that the initial code, for loop starts with 0 blocks, increases to "n" number, and the block is n-1
        print("#" * i)

if __name__ == "__main__":
    main()
'''
'''New Code Below'''
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1)) #change made here

if __name__ == "__main__":
    main()