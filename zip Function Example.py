# zip Function Example
OEM = ['Honda', 'Mazda', 'Toyota']
Model = ['Accord', 'Mazda6', 'Camry']
Cars = {}

for OEM,Model in zip(OEM, Model):
    Cars[OEM] = Model

print(Cars)
