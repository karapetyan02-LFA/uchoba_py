# Пользователь вводит целое число N,
# а компьютер, если N >= 0, рисует ромб
# по следующей схеме (ромб состоит из
# 2*N-1 строк):

N = input('Введите число')
N = int(N)

romb = 2*N-1

for _ in range (N):
    print(' ' * romb, end='')    
    print('#', end='')
    print(' ' * (2 * (2*N - romb) - 1), end='')
    print('#')
    romb -=1
romb += 2  
for _ in range (N):
    print(' ' * romb, end='')    
    print('#', end='')
    print(' ' * (2 * (2*N - romb) - 1), end='')
    print('#')
    romb +=1    

print()

romb = 2*N-1

for _ in range (N):
    print(' ' * romb, end='')
    print(' ' * romb, end='')
    print('#')
    romb +=1


# Пользователь вводит целое число N,
# а компьютер, если N >= 0, рисует квадрат
# N на N по следующей схеме:

N = input('Введите число')
N = int(N)

kvadrat = N*N
for _ in range (N):
    print(' ' * kvadrat, end='')
    print('#' * N)
    