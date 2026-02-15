import re

def normalize_phone(phone_number):
    
    numbers = re.sub(r'\D', '', phone_number)
    
    if numbers.startswith('380'):

        result = '+' + numbers
    else:
        result = '+38' + numbers
    
    return result

test_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
]

for number in test_numbers:
    print(f"{number} -> {normalize_phone(number)}")