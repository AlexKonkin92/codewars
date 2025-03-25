def spin_words_new(sentence):
    sent_new = sentence.split()
    lst = []
    for i in sent_new:
        if len(i) >= 5:
            lst.append(i[::-1])
        else:
            lst.append(i)
    return " ".join(lst)


sentence = "This is"
print(spin_words_new(sentence))
