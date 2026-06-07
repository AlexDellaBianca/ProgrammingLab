my_var = "ciao"


try:
    my_var = float(my_var)
except ValueError as e:
    print(f"male", {e})

raise Exception("MESA")


print("continua")

