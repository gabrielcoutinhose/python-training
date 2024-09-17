name_one = "GaBRiel"
name_two = "De lucca"
cpf_one = " 241 212, 3,437"
cpf_two = "333,  322 1.223"

print(f"{name_one.upper().strip()}: {cpf_one.replace(",","").replace(".", "").replace(" ","")}")
print(f"{name_two.upper().strip()}: {cpf_two.replace(",","").replace(".", "").replace(" ","")}")
