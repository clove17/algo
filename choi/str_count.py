user_input1 = raw_input()
user_input2 = raw_input()

str_count = 0

#다음과 같이 간단히 list로 Casting 가능하다.
for i in list(user_input1):
	if(i == user_input2):
		str_count += 1
		
print (str_count)