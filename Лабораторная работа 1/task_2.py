# TODO Найдите количество книг, которое можно разместить на дискете
stroka = 25
v_stranice = stroka * 50
v_knige = v_stranice * 100
value_na_knigu = v_knige * 4
value = 1.44 * 1024 * 1024
skolko_knig = value/value_na_knigu
print("Количество книг, помещающихся на дискету:", int(skolko_knig))
