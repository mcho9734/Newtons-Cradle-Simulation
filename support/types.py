
from vpython import box, cylinder, sphere, vector

from typing import Any, TypedDict

VPythonColor = vector
VPythonTexture = str
Pendulum = tuple[box, sphere, cylinder]

class PendulumEntry(TypedDict):
    mass: str
    restitution_coeffs: str
    color: str
    texture: str
    objects: Pendulum
    theta: float
    omega: float
    