## A pangram is a sentence that contains all 26 letters of the English alphabet at least once.

print("Enter String:")
s = input().lower()
letters = set()
for ch in s:
    if 'a' <= ch <= 'z':
        letters.add(ch)
if len(letters) == 26:
    print("Pangram")
else:
    print("Not a Pangram")
