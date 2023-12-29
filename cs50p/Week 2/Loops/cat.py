x = 0
while x < 3:
    print("meow")
    x = x + 1

'''
I wrote the above without watching through the video, the video initially writes:

i = 3
while i != 0:
    print("meow")
    i = i - 1
'''

'''
Lets get fancy
'''

print("We are getting fancy here (This isn't part of the lecture)")
def meow(x):
    while x > 0:
        print("Meow")
        x = x - 1

def main():
    count = input("How many times do you want the cat to meow?: ")
    count = int(count)
    meow(count)

main()
