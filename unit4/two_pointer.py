def is_prime(n):
    '''input a number, and return a boolean indicating
    whether the number is a prime number or not
    
    IOCE 
        input: number
        output: boolean -> True is the number is prime
        constraints/considerations
            we should use a while loop
            there is not a minimum number that indicates a prime number
            e
            is there a range of numbers the input will be in
        example
            2 -> True
            101 -> True
            54 -> False 
    Plan
        create an incrementer variable that will be used
        to divide the input number by the incrementer var
        what will the stopping condition be ?
            stopping condition: incrementer >= input

        '''
    #initialize the incrementer variable
    k = 1
    while n > k:
        k +=1
        #if the remainder is zero then the numbers are divisible
        if n % k == 0 and k < n:
            return True, k
    return False

# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(45))

def reverse_list_two_point(lst):
    '''
    IOCE
        input: list of integers or characters
        output: reverse of the input list
        constraints/considerations: 
            does the input list just have integers or are there other datatypes
        examples:
            [1,2,3,4,5] -> [5,4,3,2,1]
    Plan
        create 2 pointer variables
        have a while loop for when the pointers are not crossed
            swap the values at lst[pointer] for each pointer 
            head++ and tail--     '''
    head = 0
    tail = len(lst) - 1
    while head < tail:
        temp = lst[head]
        lst[head] = lst[tail]
        lst[tail] = temp
        head += 1
        tail -= 1
    return lst
#print(reverse_list_two_point([1,2,3,4,5]))

def reverse_list(lst):
    '''the goal of this function is to find a more efficient algorithm
    for finding the reversed version of the input list'''
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
    return reversed_lst
#print(reverse_list([3,4,5,6,7,78]))


def sort_array_by_parity(nums):
    '''
    IOCE
        input: nums -> integer list
        output: int list with all even numbers before odd numbers
        constraints: 
            all of the integers are whole numbers
            any exceptions to be thrown?
            the order of the even numbers and odd numbers does NOT matter,
                as long as the even numbers are before the odd numbers
            will we have duplicates?
        examples:
            [3,1,2,4] -> [2,4,3,1]
    Plan
        have a 2-pointer loop that checks the parity of each number
        and either append if odd or add to the front if even

        '''
    head, tail = 0, len(nums) - 1
    parity_nums = []
    while head < tail:
        #if head pointer is even, add to front, else append
        if nums[head] % 2 == 0:
            parity_nums.insert(0, nums[head])
        else:
            parity_nums.append(nums[head])
        
        #if tail ptr is even, addFront, else append
        if nums[tail] % 2 == 0:
            parity_nums.insert(0, nums[tail])
        else:
            parity_nums.append(nums[tail])
        head += 1
        tail -= 1
    #account for when head==tail
    if nums[head] % 2 == 0:
        parity_nums.insert(0, nums[head])
    else:
        parity_nums.append(nums[head])
    return parity_nums
print(sort_array_by_parity([3,5,43,66,788,23,12]))
#expectation: [66,788,12,43,23,5,3]


def first_palindrome(words):
    '''
    IOCE
        input: words -> list of strings
        output: string -> first palindrome in the words list
        considerations:
            check whether each string is a palindrome until we find one
            return an empty string if there is no palindrome found
        examples: 
            ["abc","car","ada","racecar","cool"] -> "ada'
            ["abc", "racecar", "cool"] -> "racecar" 
            ["abc", "def"] -> ""  
    Plan
        initialize a sol = '' for the no palindrome answer
        traverse through the words list
            check if word[len(word)/2 + 1] == word[:len(Word)/2 + 1:-1]
                return word

        '''
    
    palin = ""
    for word in words:
        '''I was trying to figure out an efficient was to slice the first half of the word
        and the second half of the word, this is a matter of slicing correctly'''
        # print(word[int(len(word)/2)+1:: -1])
        # if word[:int(len(word)/2) +1] == word[int(len(word)+1/2) + 1::-1]:
        #     return word
       
        if word == word[::-1]:
            return word
    return palin
# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)


def remove_duplicates(nums):
    '''
    IOCE
        input: int[] -> nums, sorted int list
        output: int -> len(distanct sorted int list)
        constraints:
            no extra space, O(1) space complexity
            remove the duplicates in-place
        examples:
            [1,1,2,3,4,4,4,5] -> [1,2,3,4,5]
    Plan
        iterate throughout sorted list, with 2 ptrs
            if prev int == curr int, remove curr int
                then increment hte 2nd ptr
                if the nums[ptr] != nums[ptr] exit loop
        return len(nums)
            '''
    i = 0
    j = 1
    while i < j and j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(i)
            j +=1
        i += 1
    return nums

print(remove_duplicates([1,1,2,3,4,4,4,5]))