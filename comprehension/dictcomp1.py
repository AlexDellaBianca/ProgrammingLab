frase_input = "the cat sat on the mat the cat"

dic_output = {s: frase_input.count(s) for s in frase_input.split(" ")}

print(dic_output)

