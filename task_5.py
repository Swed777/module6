print('Задача 5. Счастливый билетик')
print('____________________________')
# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе номер билета из четного количества цифр
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
counter = 1
summ1 = 0      # Сумма первых трех чисел
summ2 = 0      # Сумма вторых трех чисел
number = int(input('Введите число с четным количеством цифр (6): '))

while True:
  while counter <= 3:
    counter += 1
    summ2 += (number % 10)
    number = number // 10
#    print(summ2)
  while counter <= 6:
    counter += 1
    summ1 += (number % 10)
    number = number // 10
#    print(summ1)
  if summ1 == summ2:
    print('У Вас счастливый билет!') 
    break
  else:
    print('Вам не повезло. Обратитесь к кондуктору еще раз')   
    break
print('********************************************************')
 
