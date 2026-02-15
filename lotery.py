import random

def get_numbers_ticket(min, max, quantity):

    numbers = []
    
    while len(numbers) < quantity:

        new_number = random.randint(min, max)
        
        if new_number not in numbers:
            numbers.append(new_number)
    numbers.sort()
    
    return numbers
my_ticket = get_numbers_ticket(1, 49, 6)
print("Мої щасливі числа:", my_ticket)