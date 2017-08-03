
def  minEditDistR(source, target):
    """ Minimum edit distance. Straight from the recurrence. """

    i = len(target); j = len(source)

    if i == 0:  return j
    elif j == 0: return i

    return(min(minEditDistR(target[:i-1],source)+1,
              minEditDistR(target, source[:j-1])+1,
              minEditDistR(target[:i-1], source[:j-1])+substCost(source[j-1], target[i-1])))

def substCost(x,y):
    if x == y: return 0
    else: return 2


correct_word = ['cat', 'car', 'cart', 'cars', 'card', 'curd']

edit_dict = {}

input_word = 'curt'

for i in correct_word:
    edit_dict[i] = minEditDistR(input_word, i)

# print edit_dict, reduce(lambda key1, key2 : key1 if(edit_dict[key1] < edit_dict[key2]) else key2, edit_dict)
# print min(edit_dict.items(), key=lambda x:x[1])

print edit_dict, filter(lambda key: edit_dict[key] <= 2, edit_dict)
