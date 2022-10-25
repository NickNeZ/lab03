
n = int(input("Введите кол-во символов: "))
yn = int(input("1 - по возрастанию\n2 - по убыванию\nВаш выбор: "))


ls = []
for i in range(n):
    ls.append(i)
    ls[i]= int(input(f"Введите {i+1} число: "))

for i in range(n-1):
    for j in range(n - i - 1):
        if yn == 1:
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
        else:
            if ls[j] < ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]

print(ls)