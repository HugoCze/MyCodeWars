

# counts = dict()
# for i in items:
#   counts[i] = counts.get(i, 0) + 1

def change_to_parenteses(word):
    new_string = ""
    count_letters = dict()
    for l in word:
            count_letters[l] = count_letters.get(l, 0) + 1
    for key, value in count_letters.items():
        if value <= 1:
            new_string + "("
        else:
            new_string + ")"
    print(new_string)

change_to_parenteses("dinn")