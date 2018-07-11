# dict
a = {"num1":10, "num2":39, "num3":21}
print(a)

b = {}
for i in range(0,3) :
	k = input("input key : ")
	v = int(input("input value : "))
	b[k] = v
print(b)

sear = int(input("I wanna find the number : "))
print(sear in b.values())
if sear in b.values() :
	print("It is in the dict{}!")
else :
	print("No, it is not in dict{}.")