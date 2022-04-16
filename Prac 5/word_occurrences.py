text = input('Text:')
sorted_words = sorted(text.split(" "))
count_occurrences = {word: sorted_words.count(word) for word in sorted_words}
for word in count_occurrences:
    print("{:10} : {}".format(word, count_occurrences[word]))
