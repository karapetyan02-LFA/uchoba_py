# Дана скорость и расстояние двух автомобилей: speedo и distance. Нужно найти: time первой машины и второй.
speedo1 = input('Введите скорость первой машины : ')
speedo1 = int(speedo1)

distance1 = input('Введите расстояние первого автомобиля : ')
distance1 = int(distance1)

print('time 1 : %f' % (distance1 / speedo1 ))

speedo2 = input('Введите скорость второй машины : ')
speedo2 = int(speedo2)

distance2 = input('Введите расстояние второго автомобиля : ')
distance2 = int(distance2)

print('time 2 : %f' % (distance2 / speedo2 ))


#Когда машины будут разьезжаться в противоположном напрвлении.
    
speedo1 = input('Введите скорость первой машины : ')
speedo1 = int(speedo1)

speedo2 = input('Введите скорость второй машины : ')
speedo2 = int(speedo2)

distance = input('Введите расстояние мужду автомобилями : ')
distance_2 = input('Введите расстояние спустя некоторое время, пример: 30 минут') 
distance = int(distance)
distance_2 = int(distance_2)
print('time 2 : %f' % ((speedo1 + speedo2) / distance ))
while  distance < distance_2:
    if distance < distance_2:
        print('Машины не встертятся')
