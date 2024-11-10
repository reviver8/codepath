import string
def swap_ends(str):
    return str[-1]+str[1:-1]+str[0]

str = "boat"
swapped = swap_ends(str)
#print(swapped)

def is_pangram(pan_str):
    '''Return a boolean indicating whether the string passed in is a pangram.
    A pangram contains every letter in the English alphabet.'''
    # return pan_str.lower() in list(string.ascii_lowercase)
    # we can iterate throughout the input string and put all prev letters into 
    # it is important to account for the the cases of the characters and miscelaneous symbols
    # additoin
    pan_str = pan_str.lower()
    pan_str = pan_str.replace(" ", "")
    prev_chars = []
    for character in pan_str:
        if character not in prev_chars and character not in "[.!,;'/\]":
            prev_chars.append(character)
    return len(prev_chars) == 26

pan_str1 = "The quick brown fox jumps over the lazy dog"
#print(is_pangram(pan_str1))

pan_str2 = "The dog jumped"
#print(is_pangram(pan_str2))

pan_str3 = "When zombies arrive, quickly fax Judge Pat."
#print(is_pangram(pan_str3))

def min_distance(word_list, word1, word2):
    '''return the minimum distnace between 2 words in the list,
    given that the distance between 2 adjacent words is 1'''
    # one approach: have a variable for the first word passed in the list
    # and then check to make sure the next word it not the previous word and 
    prev_word = ""
    # dist = 0
    # for word in word_list:
    #     if dist == 0:
    #         if word == word1:
    #         if word == word2:
    pass

def reverse_string(rev_str):
    '''rev_str[-1:0], str[start:end:step]'''
    return rev_str[::-1]
rev_str = "live"
print(reverse_string(rev_str))

def first_unique_char(str):
    '''return the number of characters that only appear once in str
    (IOCE)
        input: str- string to check for unique characters
        output: int- index of the first unique char or -1 if it DNE
        constraints: 1<= len(str) <= 10^5 and str will only have lowercase letters
        example:
            str = "leetcode" -> 0
            str = "codepath" -> 0
            str = "aabbb" -> -1
            str = "zzzz" -> -1
            
    plan
        init var to return (first_unique_index: int)
        for loop - iterate through string
            compare something
        for loop - check for the first qhose freq is 1
            return the index
        return -1'''
    freq_list = {}
    for char in str:
        freq_list[char] = freq_list.get(char, 0) + 1
        #dict.get(x) allows us to have a default value for x, if it is not originally in the dict
    for i, char in enumerate(str):
        if freq_list[char] == 1:
            return i
    return -1
print(first_unique_char("leetcode"))

uniq_str2 = "loveleetcode"
print(first_unique_char(uniq_str2))



def sum_of_number_strings(nums):
    sol = 0
    for num in nums:
        sol += int(num)
    return sol
nums = ["10", "20", "30"]
print(sum_of_number_strings(nums))

def remove_duplicates(nums_dups):
    '''
    IOCE
        input: int[] -> sorted list of integers
        output: int[] -> sort list with distinct integers
        constraints/considerations:
            the list is sorted
            is the list ascending or descending
            ensure efficiency with time complexity
            does the list have to be contiguous
        examples:
            nums = [1,1,1,2,3,4,4,5,6,6] -> [1,2,3,4,5,6]
            No duplicates:
                [2,3,6,67,71] -> [2,3,6,67,71] 
        
    Plan
        while    '''

    num = nums_dups[0]
    i = 1
    while (i < len(nums_dups)):

    #for i, num in enumerate(nums_dups):
        if num == nums_dups[i]:
            nums_dups.pop(i)
        else:
            '''when the current num is not equal to the next num
            then we change the pointer for the current num'''
            num = nums_dups[i]
            i+=1
    return nums_dups
        # def remove_duplicates(nums):
        #     current = nums[0]
        #     i = 1
        #     while i < len(nums) :
        #         if current == nums[i]:
        #             nums.pop(i)
        #         else:
        #             current = nums[i]
        #             i+=1
        #     return nums
# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))

nums_dup1 = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums_dup1))


def longest_uniform_substring(long_str):
    '''create a frequency map of each character without regarding case
    and then return the max(freq_map.values)
    IOCE
        input: str-> string of charcters
        output: int-> the length of the longest uniform substring
        considerations: 
            will the input only be letters
            a == A -> these are considered the same character
        examples:
            "aabbbbCdAA" -> 4
    Plan
        create freq map for each uncased letter
        return max(freq_map.values())'''
    freq_map = {}
    long_str = long_str.lower()
    for letter in long_str:
        freq_map[letter] = freq_map.get(letter, 0) + 1
    return max(freq_map.values())
    # look at the frequency map from the unique character function
    # take a look at lines 71-78



print(longest_uniform_substring("aabbbbCdAA"))
print(longest_uniform_substring("abcdef"))
