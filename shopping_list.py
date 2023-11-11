
shopping = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
    }


text = ''
number_of_products = 0
for key, value in shopping.items():
    key = key.capitalize()
    value = [i.capitalize() for i in value]
    text += f'Idę do {key}, kupuję tu następujące rzeczy: {value}\n'
    number_of_products += len(value)

info = ('Lista zakupów\n{}W sumie kupię {} produktów.'
        .format(text, number_of_products))
print(info, '\n')

print("Pierwsza zmiana")
