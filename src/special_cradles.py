"""
CS1 24fa - Assignment 4
Helper functions and implementation of a Newton's cradle simulation.
"""

from vpython import vector  # type: ignore

from src.constants import COLOR_MAP, TEXTURE_MAP

from src.pendulum import make_pendulum
from support.sheets_api import update_values, get_pendulum_info
from support.types import PendulumEntry

# TODO 1: write the following 5 functions using relevant helper functions from `sheets_api`.
def uniform_mass_newton_cradle(spreadsheet_id: str,
                               mass_range: str,
                               mass: float,
                               num_pends: int,
                               ) -> None:
    """
    Updates the spreadsheet such that all pendula have the same mass. 

    Args:
        spreadsheet_id (str): unique ID of Google Sheet
        mass_range (str): range of cells that have mass values in the spreadsheet
        mass (float): mass to be uniformly applied to each pendulum
        num_pends (int): number of pendula in the Newton's cradle
    """
    ...
    # TODO: create an empty list that will serve as the required nested list
    #  as described in the guide. Then, for each pendulum, append a list with
    # the required string mass value to the empty list
    # Then, use a helper function from `sheets_api.py` to update this nested
    # list of values to the specific spreadsheet defined by the 
    # `spreadsheet_id`


def uniform_e_newton_cradle(spreadsheet_id: str,
                            e_range: str,
                            e_val: float,
                            num_pends: int,
                            ) -> None:
    """
    Updates the spreadsheet such that all pendula have the same coefficient of
    restitution. 

    Args:
        spreadsheet_id (str): unique ID of Google Sheet
        e_range (str): range of cells that have restitution_coeffs values in the 
        spreadsheet
        e_val (float): coefficient of restitution to be uniformly applied to each 
        pendulum
        num_pends (int): number of pendula in the Newton's cradle
    """
    ...
    # TODO: similar to the previous function, but you will be updating
    # the coefficients of restitution with the relevant value instead


def elastic_newton_cradle(spreadsheet_id: str,
                          e_range: str,
                          num_pends: int,
                          ) -> None:
    """
    Updates the spreadsheet such that all pendula have perfectly elastic
    collisions with each other. 

    Args:
        spreadsheet_id (str): unique ID of Google Sheet
        e_range (str): range of cells that have restitution_coeffs values in the 
        spreadsheet
        num_pends (int): number of pendula in the Newton's cradle
    """
    ...
    # TODO: Use a helper function to update the spreadsheet with the elastic
    # coefficient of restitution value.


def inelastic_newton_cradle(spreadsheet_id: str,
                            e_range: str,
                            num_pends: int,
                            ) -> None:
    """
    Updates the spreadsheet such that all pendula have perfectly inelastic
    collisions with each other. 

    Args:
        spreadsheet_id (str): unique ID of Google Sheet
        e_range (str): range of cells that have restitution_coeffs values in the 
        spreadsheet
        num_pends (int): number of pendula in the Newton's cradle
    """
    ...
    # TODO: Use a helper function to update the spreadsheet with the inelastic
    # coefficient of restitution value.


def make_newton_cradle(ranges: str,
                       spreadsheet_id: str,
                       r_param: float,
                       theta_init: float,
                       ) -> list[PendulumEntry]:
    """
    Uses information from a specific Google Sheet to make a list of 
    dictionaries representing each pendula and their physical quantities.

    Args: 
        ranges (str): range of cells in the Google Sheet
        spreadsheet_id (str): unique ID of Google Sheet
        r_param (float): size parameter used to define pendulum components
        theta_init (float): initial angle of the first pendulum (in radians)

    Returns:
        (list[dict]): list of dictionaries, each dictionary representing a
                pendulum, with keys as physical attributes
    """
    ...
    # TODO: use a helper function from `sheets_api.py` to make a `pend_list`

    # TODO: write a `for` loop that goes through each pendulum dictionary
    # in `pend_list` and:
        # finds the bob color, bob texture, and calculates the axle position
        # makes a pendulum with the aforementioned attributes
        # assigns that pendulum as the value of the key 'pendulum'

        # initializes the value for the key 'theta' depending on the value of i
        # initializes the value for the key 'omega'
