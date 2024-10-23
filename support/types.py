
from vpython import box, cylinder, sphere, vector

from typing import Any, TypedDict


VPythonColor = vector
VPythonTexture = str
Pendulum = tuple[box, sphere, cylinder]


class PendAttrs(TypedDict):
    masses: str
    restitution_coeffs: str
    colors: str
    textures: str


class PendulumEntry(TypedDict):
    pendulum: Pendulum
    theta: float
    omega: float
    masses: str
    restitution_coeffs: str
