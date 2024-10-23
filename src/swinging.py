"""
CS1 24fa - Assignment 4
Helper functions and implementation of a Newton's cradle simulation.
"""

from vpython import (  # type: ignore
    cos,
    sin,
    vector,
)

from support.types import PendulumEntry


# TODO 2: update angular components of a pendulum with the derivation provided
def angle_update(omega: float,
                 theta: float,
                 r_param: float,
                 dt: float,
                 g: float,
                 ) -> tuple[float, float]:
    """
    Updates the angle and angular velocity of a pendulum system. 

    Args:
        omega (float): angular velocity of pendulum    
        theta (float): angle of pendulum 
        r_param (float): size parameter used to define pendulum components
        dt (float): time step of update
        g (float): gravitational acceleration

    Returns:
        (tuple[float, float]): time-updated omega, theta    
    """
    ...


# Provided
def swing_update(pend_dict: PendulumEntry,
                 r_param: float,
                 dt: float,
                 g: float,
                 ) -> None:
    """
    Updates the angle & position of the pendulum components in a single swing.

    Args:
        pend_dict (dict): represents attributes of the pendulum
        r_param (float): size parameter used to define pendulum components
        dt (float): time step of update
        g (float): gravitational acceleration
    """
    theta = pend_dict["theta"]
    omega = pend_dict["omega"]

    axle, bob, cord = pend_dict["pendulum"]

    omega_new, theta_new = angle_update(omega, theta, r_param, dt, g)
    bob.pos = axle.pos + r_param * vector(sin(theta_new), -cos(theta_new), 0)
    cord.axis = bob.pos - axle.pos

    pend_dict["theta"] = theta_new
    pend_dict["omega"] = omega_new


# TODO 3: update the swings for each pendulum in the list
def full_swing_update(pend_list: list[PendulumEntry],
                      r_param: float,
                      dt: float,
                      g: float,
                      ) -> None:
    """
    Updates the omegas for all the pendula in the cradle, updating each
    pendulum dictionary. 

    Args:
        pend_list (list): list of dictionaries, each dictionary representing a
                    pendulum, with keys as physical attributes
        r_param (float): size parameter used to define pendulum components
        dt (float): time step of update
        g (float): gravitational acceleration
    """
    ...
