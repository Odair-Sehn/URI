entry = input().split()
a,b,c = entry
larger = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
result = (int(larger) + int(c) + abs(int(larger) - int(c))) / 2

print('%i eh o maior' % result)