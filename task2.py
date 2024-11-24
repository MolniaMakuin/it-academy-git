general = [a + b for a in 'ab' if a != 'i' for b in 'bcd' if b != 'a']
print(general)
print(general[0::2])
letters = ['1a', '2a', '3a', '4a']
lst = [x for x in letters]
print(lst)
lst.remove('2a')
print(lst)
lst.insert(1,'2a')
print(lst)