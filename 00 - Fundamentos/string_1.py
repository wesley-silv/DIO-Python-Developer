nome = "gUIlherME"

print("=" * 54)
print("\nUtilizando o método string para maiúsculos:", nome.upper()) # The \n jumper the to other line
print("\nUtilizando o método string para minúsculos:", nome.lower())
print("\nUtilizando o método string para titulos:", nome.title())
print("\n", "=" * 54)

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") # This method remove the white spaces inside a string
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu).upper())
print("\n", "/".join(menu).upper())
