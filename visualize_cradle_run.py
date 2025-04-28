"""
Helper functions and implementation of a Newton's cradle simulation.
"""

from vpython import mag, scene, rate

from support.types import PendulumEntry
from support.constants import NC_FP, DT, GRAV, R, THETA_INIT
from src.pds_helper import write_to_csv
from src.special_cradles import uniform_mass_newton_cradle, uniform_e_newton_cradle, elastic_newton_cradle, inelastic_newton_cradle, make_newton_cradle
from src.swinging import full_swing_update

scene.title = "Newton's cradle"

def handle_collision(e: float, 
                     omega1: float, 
                     omega2: float,
                     m1: float, 
                     m2: float, 
                     r_param: float) -> tuple[float, float]:
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
    # TODO 4: Use the physics derivation provided to update velocities post collision
    ...


def handle_two_bobs(pend1: PendulumEntry, 
                    pend2: PendulumEntry, 
                    r_param: float) -> None:
    """
    Handles the collisions and updates of 2 pendula in the cradle.

    Args:
        pend1 (PendulumEntry): dictionary representing 1st pendulum, 
                        with keys as physical attributes
        pend2 (PendulumEntry): dictionary representing 2nd pendulum, 
                        with keys as physical attributes
        r_param (float): size parameter used to define pendulum components
    """
    # TODO 5: Handle pairwise pendulum motion and collisions
    ...


def newton_cradle_tick(pend_list: list[PendulumEntry], 
                       r_param: float, 
                       dt: float, 
                       g: float) -> None:
    """
    Performs one 'tick' of the entire Newton's cradle (propagates any
    motion throughout all the pendula).

    Args:
        pend_list (list[PendulumEntry]): list of pendulum dictionaries, 
                        with keys as physical attributes
        r_param (float): size parameter used to define pendulum components
        dt (float): time step of update
        g (float): gravitational acceleration
    """
    # TODO 6: Perform one step of the newton cradle
    ...


if __name__ == "__main__":
    # TODO 7.1: use a helper function to make pend_list with
    #   a filepath called NC_FP, R and THETA_INIT
    pend_list = ...

    done = False
    while not done:
        rate(1/DT)  # The rate to be included in the animation

        # TODO 7.2: Use another helper function to perform a timestep of the
        # Newton's cradle
