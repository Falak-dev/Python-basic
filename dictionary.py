sentence = "now is the time for all good people to come"
sentence += " to the aid of their party"
words = sentence.split(' ')
words = sorted(words)
print("sentence in sorted order:\n")
print(words)
numwords = {}
for i in range(0, len(words)):
    if words[i] in numwords:
        numwords[words[i]]+=1
    else:
        numwords[words[i]]=1
print("words list and count:\n")