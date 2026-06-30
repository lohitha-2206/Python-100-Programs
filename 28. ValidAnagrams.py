## Two strings are anagrams if they contain the same characters with the same frequency, but possibly in a different order.

from collections import Counter
print("Enter two strings:")
a=input()
b=input()
if sorted(a)==sorted(b) and Counter(a)==Counter(b):
    print("Anagrams")
else:
    print("Not Anagrams")
