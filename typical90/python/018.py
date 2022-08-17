from __future__ import annotations

from typing import Literal

import numpy as np

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())


def calc_angle_of_depression(coords: tuple[Literal[0], np.floating, np.floating], x: int, y: int) -> np.floating:
    cos_theta = (x ** 2 + (y - coords[1]) ** 2) / (x ** 2 + (y - coords[1]) ** 2 + coords[2] ** 2) ** 0.5
    return np.arccos(cos_theta)


def calc_coords(T: int, t: int) -> tuple[Literal[0], np.floating, np.floating]:
    w = 360 / T
    return (0, np.cos(w * t), np.sin(w * t))


for _ in range(Q):
    e_i = int(input())
    coord_i = calc_coords(T, e_i)
    angle_of_depression = calc_angle_of_depression(coord_i, X, Y)
    print(angle_of_depression)
