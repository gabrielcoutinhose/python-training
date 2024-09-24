import random

face_or_crown = ["face", "crown"]

result = random.choices(face_or_crown)

print(f"{result[0]}")  # Imprime o resultado como uma string

if result[0] == "face":  # Acessa o primeiro elemento da lista
    print("If I were you, I'd go to the nearest slot machine!")
else:
    print("Who knows next time?")
