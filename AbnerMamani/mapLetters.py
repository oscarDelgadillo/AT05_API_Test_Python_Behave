

def stringToMap(word):
    word=word.lower()
    map={}
    for i in range(0, len(word)-1):
        if not(word[i]==" "):
            map[word[i]]=word.count(word[i])
    map = sorted(map.items())
    return map

word="ThiS is String with Upper and lower case Letters"
print(stringToMap(word))