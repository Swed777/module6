print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
pay = 0 #текущий счет клиента
name = input('Как Вас зовут? '         )
debt = int(input('Сколько Вы должны? ' ))
print(name, ', Ваша задолженность составляет', debt, 'рублей')
while pay < debt:
  pay = int(input('Сколько Вы готовы внести прямо сейчас? '))
  if pay < debt:
    print('Маловато,', name,'. Давайте еще раз')
print('Отлично,', name,'! Вы погасили долг. Спасибо!')  

print('****************************************************************')