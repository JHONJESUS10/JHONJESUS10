a=[int(input(f"listanum1{i+1}lista1:")for i in range (5))]
b=[int(input(f"listanum2{i+1}lista2:") for i in range (5))]

print([a[i] * b[i] for i in range(5)])