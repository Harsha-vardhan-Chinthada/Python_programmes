s = ('a quick brown fox jumps over a lazy dog')
d = {}
for c in s :
    if c in d.keys() :
        d[c] = d[c]+1
    else :
        d[c] = 1
for k, v in d.items() :
   print('{} is {} time appeared in the sentence'.format(k,v))

