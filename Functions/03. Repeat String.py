def repeated_word(string, number_of_rows):
    result = ""
    for i in range(number_of_rows):
        result += string
    return result


word = input()
number_of_loops = int(input())
print(repeated_word(word, number_of_loops))

