from django.http import HttpResponse
import random
from datetime import datetime


def index(request):
    return HttpResponse("Добро пожаловать в библиотеку!")

def about(request):
    return HttpResponse("Это страница о нашей библиотеке.")

def time_message(request):
    now = datetime.now()
    hour = now.hour  

    if hour < 12:
        message = "Сейчас утро "
    elif 12 <= hour < 14:
        message = "Сейчас обед "
    elif 15 <= hour < 20:
        message = "Сейчас вечер "
    else:
        message = "НОЧЬ"

    return HttpResponse(message)

def random_quote(request):
    quotes = [
        "Чтобы быть незаменимой, нужно всё время меняться. — Коко Шанель",
        "Мода — это нечто, что уходит и возвращается, а стиль вечен. — Ив Сен-Лоран",
        "Стиль — это способ сказать, кто ты есть, не говоря ни слова. — Рейчел Зоуи",
        "Я всегда выбираю то, что заставляет меня чувствовать себя уверенно. — Виктория Бекхэм",
        "Не бойтесь быть смелыми — смелость всегда в моде. — Диана фон Фюрстенберг",
    ]
    quote = random.choice(quotes)
    return HttpResponse(quote)