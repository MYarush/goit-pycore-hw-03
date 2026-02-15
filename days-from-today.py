from datetime import datetime

def get_days_from_today(date):
    """
    Рахує скільки днів пройшло від заданої дати до сьогодні
    """
    date_from_user = datetime.strptime(date, '%Y-%m-%d').date()
    date_today = datetime.today().date()
    result = date_today - date_from_user
    
    return result.days

print("Днів пройшло з 2020-10-09:", get_days_from_today('2020-10-09'))
print("Днів пройшло з 2025-12-31:", get_days_from_today('2025-12-31'))