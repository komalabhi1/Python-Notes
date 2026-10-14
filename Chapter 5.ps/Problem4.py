# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(s)

print(len(s)) # 2

# so length of s is 2.

# because 20==20.0 ko python same value samzata hain
# 1==1.0
# 3==3.0