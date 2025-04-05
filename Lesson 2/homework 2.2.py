x = int(input("Enter a 5-digit number: "))
a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10
d = (x // 1000) % 10
e = (x // 10000) % 10

print (a,b,c,d,e)

x = int(input("Enter a 5-digit number: "))

print(
    (x % 10) * 10000 +
    ((x // 10) % 10) * 1000 +
    ((x // 100) % 10) * 100 +
    ((x // 1000) % 10) * 10 +
    ((x // 10000) % 10))