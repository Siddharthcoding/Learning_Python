s = set()

s.add(20)
s.add(20.0)
s.add('20')

print(len(s)) # 2 as 20 and 20.0 are considered the same
print(s)