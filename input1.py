from datetime import datetime, timedelta

def timetoB(date):
    date = datetime.strptime(date, "%d-%m-%Y") 
    today = datetime.now()  

    next_birthday = datetime(today.year, date.month, date.day)

    if (today.month, today.day) >= (date.month, date.day):
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today

    giorni = delta.days
    ore = delta.seconds // 3600
    minuti = (delta.seconds % 3600) // 60
    secondi = delta.seconds % 60

    # Stampa il tempo mancante
    print(f"Mancano {giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi al tuo prossimo compleanno.")

timetoB("11-07-2005")
