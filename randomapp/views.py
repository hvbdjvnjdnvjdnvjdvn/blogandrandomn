from django.http import HttpResponse
from django.shortcuts import render
from random import randint, choice
import logging
import pandas as pd
from . import models, forms



logger = logging.getLogger(__name__)


def log(futc):
    def wrapper(*args, **kwaegs):
        result = futc(*args, **kwaegs)
        result_for_log = str(*result).replace("b'<h1>", "").replace("</h1>'", "")
        logger.info(
            f"Была запущена функция{futc.__name__}, которая вернула {result_for_log}"
        )
        return result

    return wrapper


def get_html_table(data):
    table = []
    for i, el in enumerate(data, 1):
        table.append({"chanse": i, "result": el})
    return pd.DataFrame(table).to_html(index=False)


@log
def coin(request, count):
    coin_sides = "tails", "heads"
    result_list = []
    for _ in range(count):
        coin_flip_result = choice(coin_sides)
        coin_flip = models.CoinFlip(side=coin_flip_result)
        result_list.append(coin_flip_result)
        coin_flip.save()
        result = get_html_table(result_list)
    return render(request, "randomapp/random.html", {"table": result})


def cihoise_game(request):
    if request.method == "POST":
        form = forms.RandomForm(request.POST)
        if form.is_valid():
            game_title = form.cleaned_data["game_title"]
            tries = form.cleaned_data["tries"]
            if game_title == "C":
                return coin(request, tries)
            if game_title == "D":
                return dice(request, tries)
            if game_title == "N":
                return dice(request, tries)
    else:
        form = forms.RandomForm()
    return render(
        request, "randomapp/cihoise_game.html", {"form": form}
    )


@log
def dice(request):
    return HttpResponse(f"<h1>{randint(1, 6)}</h1>")


@log
def random_number(request):
    return HttpResponse(f"<h1>{randint(1, 100)}</h1>")


@log
def log_main(request):
    return HttpResponse("<h1>Главная страница сайта</h1>")


@log
def log_page(request):
    return HttpResponse("<h1>Страница о сайте</h1>")
