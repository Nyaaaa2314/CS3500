import random

r = random.randint(0,51)

print("Random card is: ", r)

#print(r % 13)
match r % 13:
    case 0:
        print("Ace", end=" ")
    case 1:
        print("Two", end=" ")
    case 2:
        print("Three", end=" ")
    case 3:
        print("Four", end=" ")
    case 4:
        print("Five", end=" ")
    case 5:
        print("Six", end=" ")
    case 6:
        print("Seven", end=" ")
    case 7:
        print("Eight", end=" ")
    case 8:
        print("Nine", end=" ")
    case 9:
        print("Ten", end=" ")
    case 10:
        print("Jack", end=" ")
    case 11:
        print("Queen", end=" ")
    case 12:
        print("King", end=" ")

match r // 13:
    case 0:
        print("of Clubs")
    case 1:
        print("of Diamonds")
    case 2:
        print("of Hearts")
    case 3:
        print("of Spades")

