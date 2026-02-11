paranoid_android = "Marvin, the Paranoid Android" # strings are immutable
letters = list(paranoid_android) #lists are mutable
for char in letters[:6]:
    print('\t',char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
print()
for char in letters[12:20]:
    print('\t' *3, char)