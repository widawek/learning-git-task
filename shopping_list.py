
shopping = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
    }


text = ''
for key, value in shopping.items():
    key = key
    text += f'Idę do {key}, kupuję tu następujące rzeczy: {value}\n'

print(text)
