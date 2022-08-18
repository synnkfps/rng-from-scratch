# First concept, creates a giantic number.

s = str(len(bytes(0x0fffffff))**len(bytes(0xff09)))
# print(s)
l = []

for i in s:
    l.insert(0, i)
    if len(l)>3:
        l.pop(-1)

print('\n', l)
