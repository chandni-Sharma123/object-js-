a=['chandni','sharma','kumari']
# i=0
# string=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]==a[i][0]:
#             capital=a[i][j].upper()
#             string=string+"."+capital
#         j=j+1
#     i=i+1
# print(string[1:])



# for i in a:
#     for j in i:
#         print(j)
#         break






# n=int(input("enter the number --"))
# count=0
# while n>0:
# 		count=count+1
# 		n=n//10
# print("digit",count)




# def countCountry(csv1):
#     count = 0
#     for item in csv1:
#         if '/V+' in item[0]:
#             count +=1
#     return count
# countCountry(c)



# def countCountry(csv1):
#     count = 0
#     for item in csv1:
#         if item[0].startswith('v'):
#             count +=1
#     return count

# print (countCountry(['vikas','chandn','vijay']))

def rv(str1):
	v = ""
	for c in str1:
		if c in "aeiouAEIOU":
			v += c
	rs= ""
	for c in str1:
		if c in "aeiouAEIOU":
			rs += v[-1]
			v = v[:-1]
		else:
			rs += c
	return rs
print(rv("hello"))
