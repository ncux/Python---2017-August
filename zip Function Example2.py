# zip Function Example with Comprehension

OEM = ['Honda', 'Mazda', 'Toyota']
Model = ['Accord', 'Mazda6', 'Camry']

Cars = {OEM:Model for OEM, Model in zip(OEM,Model)}


print(Cars)


