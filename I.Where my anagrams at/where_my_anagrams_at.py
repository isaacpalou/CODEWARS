def anagrams(word, words):
    list_anagrams = []
    for elemento in words:
        if sorted(word) == sorted(elemento):
            list_anagrams.append(elemento)
    return list_anagrams
