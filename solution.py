import math
from typing import Tuple, Union
import random

from models.colour import Colours

ITEMS_COUNT = 100
COLOUR_PROBABILITY = [0.7, 0.25, 0.1]  # blue, green, red


def equation_solution(a: float, b: float, c: float) -> Union[Tuple[float, float], float]:
    """Возвращает решение для формулы a*x^2 + b^x + c = 0"""
    # Решаем уравнение через дискриминант
    discr = b ** 2 - 4 * a * c
    result = None

    if discr == 0:
        result = -b / (2 * a)
    elif discr > 0:
        x1 = (-b + math.sqrt(discr)) / 2 * a
        x2 = (-b - math.sqrt(discr)) / 2 * a
        result = (x1, x2)

    return result


def mr_randomizer():
    choices = [colour.value for colour in Colours]
    random_colours = random.choices(choices, weights=COLOUR_PROBABILITY, k=ITEMS_COUNT)
    return random_colours
