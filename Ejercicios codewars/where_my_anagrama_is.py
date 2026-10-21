def anagrams(word, words):
     Anagramas = []
    
     for palabra in (words):
        if sorted(palabra) == sorted(word):
            Anagramas.append(palabra) 
     return Anagramas