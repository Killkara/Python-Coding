import random
first = ["Коллеги, ", "В то же время, ", "Однако, ", "Тем не менее, ",
         "Следовательно, ", "Соответственно, ", "Вместе с тем, ", "С другой стороны, "]
second = ["парадигма цифровой экономики ", "контекст цифровой трансформации ", "диджитализация бизнес-процессов ", "прагматичный подход к цифровым платформам ",
          "совокупность сквозных технологий ", "программа прорывных исследований ", "ускорение блокчейн-транзакций ", "экспоненциальный рост Big Data "]
third = ["открывает новые возможности для ", "выдвигает новые требования ", "несёт в себе риски ", "расширяет горизонты ",
         "заставляет искать варианты ", "не оставляет шанса для ", "повышает вероятность ", "обостряет проблему "]
fourth = ["дальнейшего углебления ", "бюджетного финансирования ", "синергетического эффекта ", "компрометации конфиденциальных ",
          "универсальной коммодитизации ", "несанкционированной кастомизации ", "нормативного регулирования ", "практического применения "]
five = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.",
        "государсвенно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытый."]
def test_(first,second,third, fourth,five):
    string = random.choice(first) + random.choice(second) + random.choice(third) + random.choice(fourth) + random.choice(five)
    return string
print(test_(first,second,third, fourth,five))
#3245234512/m