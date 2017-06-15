n = int(input("Ingrese número de filas: "))
c = input("Ingrese caracter: ")

for i in range(1, n+1):
	for j in range(1, n+1):
		if i == 1 or i == n:
			print("*", end="")
		elif i == j or j == n + 1 - i:
			print("*", end="")
		elif j > i and j < n + 1 - i:
			print(c, end="")
		else:
			print(" ", end="")
	print()