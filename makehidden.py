file_name = input("What wordlist do you want to make hidden?: ")

with open(file_name, 'r') as file:
	data = file.readlines()

length = len(data)

for i in range(length):
	data[i] = "." + data[i]

with open(file_name, 'w') as file:
	file.writelines(data)
