def count_word_frequency(sentence):
    symbols = '''!"#$%&'()*,.:;<=>?@[\]^_`{|}~'''

    for char in sentence:
        if char in symbols:
            sentence = sentence.replace(char, "")

    words = sentence.lower().split()

    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    for word in sorted(word_frequency):
        print(f"{word}: {word_frequency[word]}")

sentence = input()

count_word_frequency(sentence)
