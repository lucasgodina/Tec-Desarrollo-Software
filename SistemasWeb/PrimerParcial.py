autores = ["Isaac Asimov", "Frank Herbert", "Douglas Adams"]
autores.sort(key=lambda name: name.split(" ")[-1])
print(autores)
