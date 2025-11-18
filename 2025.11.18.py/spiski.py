
numbers = [x for x in range(5, 20+1) if x % 2 != 0]
print(numbers)



# N - ввод польз-ль
# комп созд список [0, 1, 2, ..., N, ..., 2, 1, 0], если N >= 0
# комп созд список [], если N < 0
# за list comprehension +1 балл
# То есть при N = 0 будет [0]
# То есть при N = 3 будет [0, 1, 2, 3, 2, 1, 0]


N = input("Введите число: ")
N = int(N)
if N >= 0:
    part_a = [x for x in range(0, N)]
    part_b = [x for x in reversed(range(0, N + 1))]
    numbers = part_a + part_b
    print(numbers)
else:
    print([])
    
