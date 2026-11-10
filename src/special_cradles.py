"""
Helper functions and implementation of a Newton's cradle simulation.
"""

from src.pds_helper import extract_and_convert
from vpython import vector  # type: ignore
from support.constants import *
from support.pendulum import make_objects_of_pendulum  # type: ignore
from support.types import PendulumEntry

MASS: str = "mass"
THETA: str = "theta"
OMEGA: str = "omega"
OBJECTS: str = "objects"
COLOR: str = "color"
TEXTURE: str = "texture"
RESTITUTION_COEFF: str = "restitution_coeff"
FOUR: int = 4
FIVE: int = 5
POINT_ONE: float = 0.1


def uniform_mass_newton_cradle(relative_filepath: str,
                               mass: float) -> list[PendulumEntry]:
    """
    Creates a list of pendula and updates them to have the same mass.

    Args:
        relative_filepath (str): filepath to access CSV with pendula data
        mass (float): mass to be uniformly applied to each pendulum

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    output: list[PendulumEntry] = extract_and_convert(relative_filepath)
    for pend in output:
        pend[MASS] = mass
    return output


def uniform_e_newton_cradle(relative_filepath: str,
                            e_val: float) -> list[PendulumEntry]:
    """
    Creates a list of pendula and updates them to have the same coefficient of
    restitution.

    Args:
        relative_filepath (str): filepath to access CSV with pendula data
        e_val (float): coefficient of restitution to be uniformly applied to each
        pendulum

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    output: list[PendulumEntry] = extract_and_convert(relative_filepath)
    for pend in output:
        pend[RESTITUTION_COEFF] = e_val
    return output


def elastic_newton_cradle(relative_filepath: str) -> list[PendulumEntry]:
    """
    Creates a list of pendula and updates them to have perfectly elastic
    collisions with each other. 

    Args:
        relative_filepath (str): filepath to access CSV with pendula data

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    return uniform_e_newton_cradle(relative_filepath, 1)


def inelastic_newton_cradle(relative_filepath: str) -> list[PendulumEntry]:
    """
    Creates a list of pendula and updates them to have perfectly inelastic
    collisions with each other. 

    Args:
        relative_filepath (str): filepath to access CSV with pendula data

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    return uniform_e_newton_cradle(relative_filepath, 0)


def make_newton_cradle(relative_filepath: str,
                       r_param: float,
                       theta_init: float) -> list[PendulumEntry]:
    """
    Uses information from a specific CSV file to make a list of 
    dictionaries representing each pendula and their physical attributes.

    Args: 
        relative_filepath (str): relative filepath of the CSV file
        r_param (float): size parameter used to define pendulum components
        theta_init (float): initial angle of the first pendulum (in radians)

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding
        to each pendulum, with keys representing physical attributes
    """
    output: list[PendulumEntry] = extract_and_convert(relative_filepath)
    for i in range(len(output)):
        cur_pend = output[i]
        cur_pend[THETA] = 0
        if i == 0:
            cur_pend[THETA] = theta_init
        cur_pend[OMEGA] = 0
        axle_pos = vector((-POINT_ONE + r_param / FOUR * i),
                          r_param / FIVE, 0)  # type: ignore
        cur_pend[OBJECTS] = make_objects_of_pendulum(
            axle_pos, r_param, cur_pend[THETA], COLOR_MAP[cur_pend[COLOR]], TEXTURE_MAP[cur_pend[TEXTURE]])
    return output
