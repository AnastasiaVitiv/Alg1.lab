start = input(str("Введіть слово: "))
def reverse_string(input_word):
    new_list = []

    for i in range(len(input_word) - 1, -1, -1):
        new_list.append(input_word[i])

    reversed_str = ''.join(new_list)
    return reversed_str


print(reverse_string(start))
