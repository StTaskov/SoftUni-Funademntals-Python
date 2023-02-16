words_count = int(input())
dict_for_synonyms = {}

for _ in range(words_count):
    word = input()
    synonym = input()
    list_of_synonyms = [synonym]
    if word not in dict_for_synonyms:

        dict_for_synonyms[word] = list_of_synonyms
    else:
        dict_for_synonyms[word] += list_of_synonyms

for key in dict_for_synonyms:
    print(f"{key} - { ', '.join(dict_for_synonyms[key])}")