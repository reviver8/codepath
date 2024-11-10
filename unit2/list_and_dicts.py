'''We are going to practice working with lists and dictionaries throuhgout this file
   there will also be an overview of traversing through lists'''

def is_subsequence(lst, sequence):
    '''Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters.
      Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list.
        Return True if sequence is a subsequence, and False otherwise.'''
    matched_indices = []
    for list_index in range(len(lst)):
        for seq_index in range(len(sequence)):
            if sequence[seq_index] == lst[list_index]:
                matched_indices.append(list_index)
    
    return (sorted(matched_indices) == matched_indices) and (len(matched_indices) == len(sequence))

            
    # if len(sequence) == 0:
    #   return True 
    # if len(sequence) > len(lst): 
    #   return False 
    # seq_index = 0 
    # for num in lst: 
    #   if num == sequence[seq_index]: 
    #     seq_index += 1 
    #     if seq_index == len(sequence): 
    #       return True 
    # return False
        
def create_dictionary(keys, values):
    # new_dict = {keys: values for keys,
    #         values in zip(keys, values)}
    dictionary = dict(zip(keys, values))
    return dictionary


#either for vs code or for python, it is not necessary to write a main method to run your function
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 22, 10]
print(is_subsequence(lst, sequence))


def cast_vote(votes_dict, candidate):
    ''' write a function that casts votes to a candidate, for each vote either
      update a candidates votes or add them to the dict '''
    # update the dictionary with the new candidate vote
    # if the candidate is new add them to the dictionary with 1 vote
    # else do increment the candidate's votes
    if votes_dict.get(candidate, None) is None:
        votes_dict[candidate] = 1
    else:
        votes_dict[candidate] += 1

votes_dict = {"Alice": 5, "Bob": 3}
# cast_vote(votes_dict, "Alice")
# print(votes_dict)
# cast_vote(votes_dict, "Gina")

# cast_vote(votes_dict, "alice")
# print(votes_dict)


def common_keys(dict1, dict2):
    '''After passing in 2 dictionaries, return a list of keys they both have (order does not matter)'''
    ckeys = []
    for element in dict1.keys():
        if element in dict2.keys():
            ckeys.append(element)
    return ckeys

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
