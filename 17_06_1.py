def count_word_frequency(naxadasutyun):
    symbols = '''!"#$%&'()*,.:;<=>?@[\]^_`{|}~'''

    for char in naxadasutyun:
        if char in symbols:
            naxadasutyun = naxadasutyun.replace(char, "")

    words = naxadasutyun.lower().split()

    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    for word in sorted(word_dict):
        print(f"{word}: {word_dict[word]}")

naxadasutyun = input("Greq naxadasutyun@: ")

count_word_frequency(naxadasutyun)
