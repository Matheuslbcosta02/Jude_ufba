PALAVRA = 'incomodam, '
print("1 elefante incomoda muita gente")
for i in range(2,11):
    if i % 2 == 0:
        print(f"{i} elefantes {i * PALAVRA } muito mais")
    else:
        print(f"{i} elefantes incomodam muita gente")
