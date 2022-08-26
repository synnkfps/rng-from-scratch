# First concept, creates a giantic number.

s = 0x3f**28805 
# print(s)
l = []

for i in s:
    l.insert(0, i)
    if len(l)>3:
        l.pop(-1)

print('\n', l)
