# Find all number divisible by 7 but not a mulitple of 5 between 2000-3200
# solution be comman seprated

# Define a Empty List
lista = []

for i in range(1, 50):
    if (i%7==0) and (i%5!=0):
        lista.append(str(i))

print(','.join(lista))
