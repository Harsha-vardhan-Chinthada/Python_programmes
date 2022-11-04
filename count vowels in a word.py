sentence = input("type a sentence: ")
vowels = {'a', 'e', 'i', 'o', 'u',}
results = {}
for c in sentence :
    if c in vowels :
        results[c] = results.get(c, 0)+1
for k , v in results.items() :
    print(k,"is present", v,"times in the sentence")

