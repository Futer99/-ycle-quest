import art
print("Вы попали в игру название которой мне лень придумывать, в ней вы можете либо стать крутым либо... Эээээ забыл, что я вам вообще все разжевываю? Сами разберетись.")
print("Создайте вашего персонажа!")
name = input("Say my name: ")
laminat = input("Пол персонажа(не ламинат): ")
profesion = input("Условная професия: ")
print("Вот ваш персонаж:")
print("Имя:",name)
print("Пол персонажа:",laminat)
print("Условная професия",profesion)
input("Начать игру за этого персонажа?:")
print("Что бы ты не ответил мне все равно, радуйся что хоть не так как в Deltarune.")
start = input("Начать игру?: ")
if start == "Да" or start == "да":
 print("Тогда начнем")
elif start == "Нет" or start == "нет":
 print("Повторяю мне все равно")
else:
    print("Будем считать за да")
print("_" * 500)
print("Вы просыпаетесь, комната в которой вы проснулись кажется вам знакомой, но вы не можете вспомнить что это за место.")
print("Вы начинаете осматриваться, перед вами каменное помещение с кроватью, шкафом, письменным столом и сундуком.")
while True:
    kam_komnata = input("Напиши с чем хочешь повзаимодействовать (кровать/стол/сундук): ")
    if kam_komnata.lower() == "кровать":
        print("Вы ложитесь на кровать и засыпаете. Вы не знаете сколько прошло времени, как вдруг вы просыпаетесь... у себя в комнает?..")
        break
    elif kam_komnata.lower() == "стол":
        print("Вы осмотрели стол, вы нашли отмычку и заженную свечку, вы захотели отпереть дверь с помощью отмычки, но вдруг поняли что двери в комнате нет, вы отошли от стола и продолжили оглядываться.")
    elif kam_komnata.lower() == "сундук":
        print("Вы открыли его, на ваше удивление вы ничего не нашли в нем а внутри он выглядел кристально чистым, вы отошли от него и стали оглядываться дальше. ")
    else:
        print("Выбери один из вариантов.")
print("_" * 500)
print(art.tprint("Chapter 1"))
print("_" * 500)
print("Вы сильно удивлены этому исходу, но наверное это был сон? Если и сон то больно реалистичный... У вас возникает мысль пойти на кухню и попить воды и все обдумать.")
poity_na_kyhnu = input("Пойти на кухню(да/нет)?")
if poity_na_kyhnu.lower() == "да":
    print("Вы пошли на кухню по дороге продолжая осматривать свою квартиру, квартира была в своем обычном состоянии, вот гостиная, вот кладовка где лежат инструменты для вашей роботы", profesion, ", наконец вы дошли до кухни.")
elif poity_na_kyhnu.lower() == "нет":
    print("Вы решаете что не стоит идти на кухню и остаетесь у себя в комнате")





