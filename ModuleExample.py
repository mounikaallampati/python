import random
from random import choice,randint,shuffle
def main():
    numbers=get_number()
    print(numbers)
    coin=get_choice()
    print(coin)
    l1=["moni","vinod","mandeep"]
    l2=get_shuffledseq(l1)
    print(l1)
def get_number():
    number=randint(1,100)
    return number
def get_choice():
    return choice(["heads", "tails"])

def get_shuffledseq(l1):
    return shuffle(l1)

main()

