def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]


print(card_hide("35123413355523"))


def palindrome(slovo):
    slovo1 = slovo.lower().replace(' ', '')
    return slovo1[:] == slovo1[::-1]

print(palindrome('Довод'))
print(palindrome('Начало'))
