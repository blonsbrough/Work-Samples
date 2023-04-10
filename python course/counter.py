from collections import Counter

with open('advanced-python-concepts\Exercises\Declaration_of_Independence.txt') as f:
    D = f.read()
c = Counter(word for word in D.upper().split() if len(word)>5)
print(c.most_common(10))
    