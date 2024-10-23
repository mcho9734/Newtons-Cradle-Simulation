
from vpython import vector

from typing import Any, TypedDict


VPythonColor = vector
VPythonTexture = str


class PendAttrs(TypedDict):
    masses: str
    restitution_coeffs: str
    colors: str
    textures: str


class Pendulum(TypedDict):
    theta: float
    omega: float
    masses: float
    restitution_coeffs: float
    pendulum: tuple[Any, Any, Any]  # TODO
