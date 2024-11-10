
def double_sum(a,b):
    """return double the sum of the input integers"""
    return 2*sum(a,b)

def sum(a,b):
    """returns the sum of 2 integers"""
    return a + b

#
def what_time_is_it(hour):
    """this is the code for what time it is 
    thus problem 7 in unit 1 session 1"""
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"


def black_jack(score):
    """The following algorithm corresponds to playing blackjack, 
    thus when a player is given a certain amount of card
    the player will say a specific phrase to the dealer"""
    if score == 21:
        return "Blackjack!"
    elif score > 21:
        return "Bust!"
    elif score < 17:
        return "Hit me!"
    else:
        return "Nice hand!"
    
def get_first(arr):
    """returns the first element of a list"""
    if arr != None:
        return arr[0]
    else:
        return None
    
def counter(stop_num):
    """prints each number up until the stop_num"""
    for i in range(0, stop_num + 1, 13):
        print(i)
    
#Given a list of numbers, print all of the negative numbers
#Check whether eaech number is less than 0, if so print it
def negative_numbers(arr):
    for i, num in enumerate(arr):
        #I previously used <for i in range(len(arr)):>
        if num < 0:
            print(num)

def main():
    # print(double_sum(5,2))
    # print(what_time_is_it(2))
    # print(black_jack(22))
    # print(black_jack(15))
    print(get_first([3,1,6,7,5]))
    return counter(55)



if __name__ == '__main__':
    main()