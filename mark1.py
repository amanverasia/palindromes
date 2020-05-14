values = []
max = int(input('Enter the maximum: '))
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

def print_em(min,max):
	for i in range(min, max+1):
		lychrel = False
		n = i
		count = 0
		temp = n
		while True:
			if(is_palindrome(n)):
				print(f'{temp} went to {n} after {count} steps. Lychrel candidate: {lychrel}')
				break
			old = n
			new = reverse_adder(n)
			n = new
			count = count + 1
			if(count>500):
				lychrel = True
				break
		values.append([i,count])

def lychrel_em(min,max):
	lychrel_count = 0
	for i in range(min, max+1):
		lychrel = False
		n = i
		count = 0
		temp = n
		while True:
			if(is_palindrome(n)):
				#print(f'{temp} went to {n} after {count} steps. Lychrel candidate: {lychrel}')
				break
			old = n
			new = reverse_adder(n)
			n = new
			count = count + 1
			if(count>500):
				lychrel = True
				lychrel_count += 1
				print(f'{temp} is a possible lychrel.')
				break
	print(f'There are {lychrel_count} lycheral numbers from {min} to {max}')

print_em(1,max)
#print(values)

#lychrel_em(1,max)

