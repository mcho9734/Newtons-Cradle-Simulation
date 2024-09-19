from vpython import *
import pytest, os, sys # type: ignore
import importlib
from src.constants import *
from src.sheets_api import *

VPYTHON_COLOR_MAP = {
    'white': vector(1,1,1),
    'red': vector(1,0,0),
    'green': vector(0,1,0),
    'blue': vector(0,0,1),
    'cyan': vector(0,1,1),
    'magenta': vector(1,0,1),
    'yellow': vector(1,1,0),
    'orange': vector(1,0.6,0),
    'purple': vector(0.4,0.2,0.6),
    'black': vector(0,0,0)
}

import src.newton_cradle_run as main