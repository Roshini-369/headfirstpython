phrase = "Don't panic!"
plist = list(phrase)
print("phrase =",phrase)
print("plist =",plist)
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(),plist.pop()])
# plist.insert(2,plist.pop(3))
# new_phrase = ''.join(plist)
mod_phrase = plist[1:3]+plist[5:3:-1]+plist[7:5:-1]
new_phrase = ''.join(mod_phrase)
print(plist)
print("mod_phrase =",mod_phrase)
print("new_phrase =",new_phrase)
