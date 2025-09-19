a = int(input("Enter a value:"))
k = int(input("Enter a limit:"))
for i in range(k):
    b = str(a)
    c = b[::-1]
    d = int(c)
    a = a + d
    print(f"step{i+1} = {a} ")
    if str(a) == str(a)[::-1]:
        print("found a palindrome")
        break
