from vpython import *
import pytest, os, sys # type: ignore
from src.constants import *
from src.sheets_api import *
from tests.helpers.fake_objects import *
from tests.helpers.constants_for_testing import *

@pytest.mark.parametrize("e, omega, omega2, m1, m2, r_param, expected_omega, expected_omega2", [
    (0, 1, -1, 1, 1, 0.1, 0.0, 0.0),        # fully inelastic
    (1, 1, 0, 1, 1, 0.1, 0.0, 1.0),         # fully elastic
    (1, 0, 0, 1, 1, 0.1, 0.0, 0.0),         # no initial angle          
    (1, 2, -1, 2, 1, 0.1, 0.0, 3.0000000000000004),   # random elastic 
    (0.5, 2, -1, 2, 1, 0.1, 0.5000000000000001, 2.0000000000000004)  # random inelastic
])
def test_handle_collision(e, omega, omega2, m1, m2, r_param, expected_omega, expected_omega2):
    print(main.handle_collision(e, omega, omega2, m1, m2, r_param))
    omega_new, omega2_new = main.handle_collision(e, omega, omega2, m1, m2, r_param)
    assert omega_new == pytest.approx(expected_omega, rel=0.001)  # 0.1% relative tolerance
    assert omega2_new == pytest.approx(expected_omega2, rel=0.001)  # 0.1% relative tolerance
