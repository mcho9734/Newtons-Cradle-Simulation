"""
CS1 24fa - Assignment 4
Helper functions and implementation of a Newton's cradle simulation.
"""

from vpython import *
from src.constants import *
from src.sheets_api import get_values, update_values, get_pendulum_info
from src.pendulum import make_bob, make_axle, make_cord, make_pendulum
from src.special_cradles import uniform_mass_newton_cradle, uniform_e_newton_cradle, elastic_newton_cradle, inelastic_newton_cradle, make_newton_cradle
from src.swinging import angle_update, swing_update, full_swing_update

scene.title = "Newton's cradle"


# TODO 4: use the physics derivation provided to update velocities post collision
def handle_collision(e, omega1, omega2, m1, m2, r_param):
    """
    In case two bobs collide, handles the physics (momentum conservation).

    Args:
        e (float): coefficient of restitution for collision
        omega1 (float): angular velocity of first pendulum
        omega2 (float): angular velocity of second pendulum
        m1 (float): mass of first pendulum
        m2 (float): mass of second pendulum
        r_param (float): size parameter used to define pendulum components

    Returns:
        (tuple[float, float]): post-collision omegas of 1st, 2nd pendula
    """
    pass


# TODO 5: handle pairwise pendulum motion and collisions
def handle_two_bobs(pend1, pend2, r_param):
    """
    Handles the collisions and updates of 2 pendula in the cradle.

    Args:
        pend1 (dict): dictionary representing 1st pendulum, 
                        with keys as physical attributes
        pend2 (dict): dictionary representing 1st pendulum, 
                        with keys as physical attributes
        r_param (float): size parameter used to define pendulum components
    """
    pass


# TODO 6: perform one step of the newton cradle
def newton_cradle_tick(pend_list, r_param, dt, g):
    """
    Performs one 'tick' of the entire Newton's cradle (propagates any
    motion throughout all the pendula).

    Args:
        pend_list (list[dict]): list of pendulum dictionaries, 
                        with keys as physical attributes
        r_param (float): size parameter used to define pendulum components
        dt (float): time step of update
        g (float): gravitational acceleration
    """
    pass
        

if __name__ == "__main__":
    pend_list # TODO 7.1: use a helper function to make pend_list with
                # RANGE, SPREADSHEET_ID, R and THETA_INIT

    done = False
    while not done:
        rate(1/DT) # The rate to be included in the animation
        
        # TODO 7.2: Use another helper function to perform a timestep of the
        # Newton's cradle



