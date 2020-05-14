def reverse_adder(n):
	sum = ''
	temp = n
	while(n>0):
		sum = sum + str(n%10)
		n = n//10
	return temp + int(sum)

def is_palindrome(n):
	sum = ''
	temp = n
	while(n>0):
		sum = sum + str(n%10)
		n = n//10
	if(int(sum)==temp):
		return True

n = int(input('Enter the number: '))
count = 0
temp = n
while True:
	if(is_palindrome(n)):
		print(f'{temp} went to {n} after {count} steps')
		break
	old = n
	new = reverse_adder(n)
	n = new
	#print(new)
	count = count + 1
	print(f'Length: {len(str(n))}  Iterations: {count}')