def matching_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of havinng the same first and last letter is:\n",lst)
    return ctr

count = matching_words(['aba','cfc','xyz','jjk','kny','lkl'])
print("Number of words having first and last letter same:",count)