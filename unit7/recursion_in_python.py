def factorial(n):
    #base case
    if n == 0 or n == 1: # 0! = 1; 1! = 1
        return 1
    #recursive call
    else:
        print(f"{n}! = {n} x {n - 1}!")
        return n * factorial(n - 1) # 5 * 4! = 5!

print(factorial(4))


def sum_list(lst):
    '''
    IOCE
        input: lst -> list of numbers
        output: int -> sum of numbers in lst
        constraints/considerations
            this function should be recursive
            we should NOTT create another O(n) variable
            time complexity
            space complexity
        examples:
            [1,2,3,4,5] -> 15
    Plan
        base case: len(lst) == 1
        recursive call:
            sum_list(lst[0:-2]) + lst[-1]
        '''
    print(lst[0:-1])
    if len(lst) == 1:
        return lst[0]
    return sum_list(lst[0:-1]) + lst[-1]

#print(sum_list([1,2,3,4,5]))

def is_power_of_two():
    pass

def count_ones(lst):
    '''
    IOCE
        input: sorted list of 0s and 1s
        output: int of total number of 1s in list
        constraints:
            time complexity: O(logn)
            use something similar to binary search
        example:
            [0, 0, 0, 0, 1, 1, 1] -> 3
        '''