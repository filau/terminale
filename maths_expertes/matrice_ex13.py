def u(n):
    a = 3
    b = 8
    
    for i in range(int(n)-1):
        c = a
        a = b
        b = 5 * a - 6 * c
    
    return b



print("Valeur de n pour laquelle vous souhaitez connaître la valeur de Uₙ :")
n = input()

b = u(n)

print(f"Pour n = {n}, Uₙ = {b}.")
