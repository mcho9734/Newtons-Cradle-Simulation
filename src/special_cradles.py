"""
Helper functions and implementation of a Newton's cradle simulation.
"""

from vpython import vector
from support.pendulum import make_objects_of_pendulum
from support.constants import *
from src.pds_helper import extract_and_convert

# TODO 1: write the following 5 functions using relevant helper functions from 'pds_helper'.
def uniform_mass_newton_cradle(relative_filepath: str, mass: float):
    """
    Creates a list of pendula and updates them to have the same mass. 

    Args:
        relative_filepath (str): filepath to access CSV with pendula data
        mass (float): mass to be uniformly applied to each pendulum

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    # TODO: create a list that will serve as the required nested list
    # as described in the guide using a helper function. Then, for each pendulum, 
    # set all the mass values in the dictionary to the required argument mass value
    ...


def uniform_e_newton_cradle(relative_filepath: str, e_val: float):
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
    # TODO: similar to the previous function, but you will be updating
    # the coefficients of restitution with the relevant value instead 
    ...


def elastic_newton_cradle(relative_filepath: str):
    """
    Creates a list of pendula and updates them to have perfectly elastic
    collisions with each other. 

    Args:
        relative_filepath (str): filepath to access CSV with pendula data
    
    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    # TODO: Use a helper function to return a list of pendula with the 
    # elastic coefficient of restitution value
    ...


def inelastic_newton_cradle(relative_filepath: str):
    """
    Creates a list of pendula and updates them to have perfectly inelastic
    collisions with each other. 

    Args:
        relative_filepath (str): filepath to access CSV with pendula data
            
    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    # TODO: Use a helper function to return a list of pendula with
    # the inelastic coefficient of restitution value 
    ...


def make_newton_cradle(relative_filepath: str, r_param: float, theta_init: float):
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
    # TODO: Use a helper function from 'pds_helper.py' to make a 'pend_list'
    

    # TODO: write a 'for' loop that goes through each pendulum dictionary
    # in 'pend_list' and:
        # finds the bob color, bob texture, and calculates the axle position
        # makes a pendulum with the aforementioned attributes
        # assigns that pendulum as the value of the key 'objects'

        # initializes the value for the key 'theta' depending on the value of i
        # initializes the value for the key 'omega'
    ...