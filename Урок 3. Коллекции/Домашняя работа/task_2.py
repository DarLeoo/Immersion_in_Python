"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.(Может помочь метод translate из модуля string)
"""
import string
import collections

article_wiki = "Родился в семье пастора. Учился в гимназиях Дуйсбурга и Цюриха. " \
               "В 1847 году получил высшее образование в Цюрихе по философии и психологии." \
               " Стажировался в Боннском университете, где в 1851 году защитил докторскую диссертацию по философии и " \
               "сдал государственный экзамен для замещения должности преподавателя гимназии. " \
               "Затем четыре года преподавал " \
               "в гимназии Кёльна. С 1855 был приват-доцентом Боннского университета; читал, среди прочего, курсы " \
               "социальной статистики (первый в Германии)" \
               " и критической истории материализма. Позже он был учителем гимназии " \
               "в Дуйсбурге; протестовал против давления, которое правительство Бисмарка в эпоху конфликта старалось " \
               "оказывать на учительскую корпорацию; оставил из-за этого службу, стал журналистом и вступил, вместе" \
               " с Бебелем, в комитет конгресса немецких рабочих союзов, где действовал в духе примирения различных " \
               "направлений." \
               "Свои взгляды на социальный вопрос он изложил в небольшой книге: «Die Arbeiterfrage» (Дуйсбург, 1865)," \
               " которая в последующих изданиях разрослась в обширный трактат. Она вызвала оживленную полемику," \
               " в которой одним из главных оппонентов Ланге выступил Ойген Рихтер. С 1865 по 1866 Ланге издавал " \
               "для рабочих газету «Der Bote vom Niederrhein»; что привело к целому ряду судебных процессов;" \
               " в то же время он написал «Die Grundlegung der mathemathischen Psychologie» (Дуйсбург, 1865) и свой " \
               "главный труд, «Историю материализма»." \
               "Переехав в Швейцарию, Ланге продолжал делить своё время между философией и политикой." \
               " «Neue Beiträge z. Geschichte d Materialismus» (Винтертур, 1867) послужили ответом на " \
               "брошюру Шиллинга об «Истории материализма», а в газете «Winterthurer Landbote» Ланге поместил длинный" \
               " ряд политических и экономических статей.В 1870 он получил в Цюрихе профессуру индуктивной философии; " \
               "принимал видное участие в выработке радикально-демократической конституции Цюриха, которой был введён " \
               "референдум.В 1872 перешёл в Марбург, где учредил Марбургскую школу неокантианства." \
               " Его учеником и преемником был Герман Коген"

article_wiki = article_wiki.translate(str.maketrans('', '', string.punctuation))

article_wiki = (article_wiki.split(" "))

num = collections.Counter(article_wiki).most_common(10)
for el in num:
    print(el)








