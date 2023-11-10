
shopping = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
    }


text = ''
for key, value in shopping.items():
    key = key.capitalize()
    value = [i.capitalize() for i in value]
    text += f'Idę do {key}, kupuję tu następujące rzeczy: {value}\n'

print(text)
