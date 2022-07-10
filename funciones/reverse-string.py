def reversa(string):
#     # string_list = [letra for letra in string]
#     # string_list.reverse()                         <-- valido tambien, pero mas largo
#     # cadena_reversa = "".join(string_list)
    inversa = string[::-1]
    return inversa


cadena = input()

print(reversa(cadena))

# mayor = 0
# for x in range(10):
#     num = int(input())
#     if num > mayor:
#         mayor = num

# print(f"{mayor}")