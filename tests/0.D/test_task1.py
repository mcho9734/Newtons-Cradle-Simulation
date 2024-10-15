from vpython import *
import pytest, os, sys # type: ignore

from src.sheets_api import get_values, update_values, get_pendulum_info
from tests.helpers.fake_objects import *
from tests.helpers.constants_for_testing import *
from src.constants import *

import src.special_cradles as main

@pytest.mark.parametrize("mass",[
    (5),(2),(1)
])

def test_uniform_mass_newton_cradle(mass):
    mass_range = "A2:A9"
    actual_masses = get_values(SPREADSHEET_ID, mass_range)["valueRanges"][0]["values"]
    num_pends = len(actual_masses)

    main.uniform_mass_newton_cradle(SPREADSHEET_ID, mass_range, mass, num_pends)
    new_masses = get_values(SPREADSHEET_ID, mass_range)["valueRanges"][0]["values"]

    for new_mass in new_masses:
        assert float(new_mass[0]) == mass

    # resetting the spreadsheet to original values
    update_values(SPREADSHEET_ID, mass_range, actual_masses)


@pytest.mark.parametrize("e",[
    (0.3),(0.5),(0.8)
])

def test_uniform_e_newton_cradle(e):
    e_range = "B2:B9"
    actual_es = get_values(SPREADSHEET_ID, e_range)["valueRanges"][0]["values"]
    num_pends = len(actual_es)

    main.uniform_e_newton_cradle(SPREADSHEET_ID, e_range, e, num_pends)
    new_es = get_values(SPREADSHEET_ID, e_range)["valueRanges"][0]["values"]

    for new_e in new_es:
        assert float(new_e[0]) == e

    # resetting the spreadsheet to original values
    update_values(SPREADSHEET_ID, e_range, actual_es)


def test_elastic_newton_cradle():
    e_range = "B2:B9"
    actual_es = get_values(SPREADSHEET_ID, e_range)["valueRanges"][0]["values"]
    num_pends = len(actual_es)

    main.elastic_newton_cradle(SPREADSHEET_ID, e_range, num_pends)
    new_es = get_values(SPREADSHEET_ID, e_range)["valueRanges"][0]["values"]

    for new_e in new_es:
        assert float(new_e[0]) == 1

    # resetting the spreadsheet to original values
    update_values(SPREADSHEET_ID, e_range, actual_es)


def test_inelastic_newton_cradle():
    e_range = "B2:B9"
    actual_es = get_values(SPREADSHEET_ID, e_range)["valueRanges"][0]["values"]
    num_pends = len(actual_es)

    main.inelastic_newton_cradle(SPREADSHEET_ID, e_range, num_pends)
    new_es = get_values(SPREADSHEET_ID, e_range)["valueRanges"][0]["values"]

    for new_e in new_es:
        assert float(new_e[0]) == 0

    # resetting the spreadsheet to original values
    update_values(SPREADSHEET_ID, e_range, actual_es)


def test_make_newton_cradle_pendulum():
    pend_list = main.make_newton_cradle(RANGE, SPREADSHEET_ID, R, THETA_INIT)
    pendulum = pend_list[0]["pendulum"]
    assert isinstance(pendulum[0], box)
    assert isinstance(pendulum[1], sphere)
    assert isinstance(pendulum[2], cylinder)


def test_make_newton_cradle_attributes():
    pend_list = main.make_newton_cradle(RANGE, SPREADSHEET_ID, 0.4, -20 * pi / 180)

    pend_data = get_pendulum_info(RANGE, SPREADSHEET_ID)

    for i in range(len(pend_list)):
        pend_dict = pend_list[i]
        sheet_pend_dict = pend_data[i]

        bob = pend_dict["pendulum"][1]
        assert VPYTHON_COLOR_MAP[sheet_pend_dict["colors"]] == bob.color # checking if bob color is implemented correctly
        texture = sheet_pend_dict["textures"]
        assert f":{texture}_texture.jpg" == bob.texture # checking if bob texture is implemented correctly

        axle_pos = pend_dict["pendulum"][0].pos
        assert axle_pos.x == pytest.approx(0.1 * i - 0.1, rel=0.01)
        assert axle_pos.y == pytest.approx(0.08, rel=0.01)
        assert axle_pos.z == pytest.approx(0.0, rel=0.01)

        assert pend_dict["theta"] == (-20 * pi / 180 if i == 0 else 0) # checking theta initialisation
        assert pend_dict["omega"] == 0 # checking omega initialisation

        assert pend_dict["masses"] == sheet_pend_dict["masses"]
        assert pend_dict ["restitution_coeffs"] == sheet_pend_dict["restitution_coeffs"]
