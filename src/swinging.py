"""
Helper functions and implementation of a Newton's cradle simulation.
"""


from vpython import (  # type: ignore
    cos,  # type: ignore
    sin,  # type: ignore
    vector,  # type: ignore
)
from support.types import PendulumEntry

THETA: str = "theta"
OMEGA: str = "omega"
OBJECTS: str = "objects"


def angle_update(omega: float,
                 theta: float,
                 r_param: float,
                 dt: float,
                 g: float) -> tuple[float, float]:
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
    new_omega = omega - (g * sin(theta) / r_param) * dt  # type: ignore
    new_theta = theta + new_omega * dt  # type: ignore
    return (new_omega, new_theta)  # type: ignore

# Provided


def swing_update(pend: PendulumEntry,
                 r_param: float,
                 dt: float,
                 g: float) -> None:
    """
    Updates the angle & position of the pendulum components in a single swing.

    Args:
        pend_dict (dict): represents attributes of the pendulum
        r_param (float): size parameter used to define pendulum components
        dt (float): time step of update
        g (float): gravitational acceleration
    """
    theta = pend[THETA]
    omega = pend[OMEGA]

    axle = pend[OBJECTS][0]  # type: ignore
    bob = pend[OBJECTS][1]  # type: ignore
    cord = pend[OBJECTS][2]  # type: ignore

    new_vals = angle_update(omega, theta, r_param, dt, g)
    omega_new = new_vals[0]
    theta_new = new_vals[1]
    bob.pos = axle.pos + r_param * \
        vector(sin(theta_new), -cos(theta_new), 0)  # type: ignore
    cord.axis = bob.pos - axle.pos  # type: ignore

    var1 = theta_new
    var2 = omega_new
    pend[THETA] = var1
    pend[OMEGA] = var2


def full_swing_update(pend_list: list[PendulumEntry],
                      r_param: float,
                      dt: float,
                      g: float) -> None:
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
    for pend in pend_list:
        swing_update(pend, r_param, dt, g)
