sentence = input("please enter a senence: ")


def most_word(string):
    l = []
    words = string.split()
    for i in words:
        if (i, words.count(i)) not in l:
            l.append((i, words.count(i)))
    sorted_words = sorted(l, key=lambda s: s[1], reverse=True)
    for j in sorted_words[:3]:
        print(j[0], j[1])


most_word(sentence)
