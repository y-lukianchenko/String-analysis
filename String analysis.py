string = "'Денис даёт нам классные задачки, которые помогут нам найти лучшую работу.'"
letter = "о"
{letter:string.count(letter) for letter in set(string)}
print(string)
print("В строке:", string, " - символ", letter, "повторяется", string.count(letter), "раз(а).")
