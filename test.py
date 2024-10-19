import pytest
import os
from io import StringIO
import sys
import re


def clear():
    """
    Clears the terminal screen.
    """
    print("\033c", end="", flush=True)


clear()

for f in sorted(set(os.listdir('tests')) - set(['__pycache__', '__init__.py', 'helpers'])):
    print(f.split(".")[-1] + " Tests: ")
    for t in sorted(set(os.listdir(os.path.join('tests/' + f))) - set(['__pycache__'])):
        sys.stdout = result = StringIO()
        code = pytest.main(["-vv", "--color=yes", "--no-header", "--disable-warnings", "-rNs", "-x"] +
                           [os.path.join('tests', f, t)], ['pytest_clarity'])
        sys.stdout = sys.__stdout__
        if code == 0:
            print("  " +
                  "\x1b[0m\x1b[32mPASSED\x1b[0m " + t.replace(".py", ""))
            continue

        before = 0
        skip = 0
        i = 0
        lines = result.getvalue().splitlines()[3:]
        while i < len(lines):
            line = lines[i].replace("LHS", "CORRECT").replace(
                "RHS", "YOURS").replace("[pytest-clarity diff shown]", "")
            if 'collecting' in line or '================' in line or '!!!!!!!' in line:
                i += 1
                continue
            if '@pytest' in line:
                before = 1
            if line.startswith("------"):
                line = line[4:-4]
            if line.startswith(os.path.join('tests', f, t)):
                line = line.replace(os.path.join(
                    'tests', f, t) + "::", "")
                if "PASSED" not in line:
                    i += 5
            if line.startswith('\x1b[1m\x1b[31mE       '):
                before = 2

            if before < 1 or before > 1:
                print('    ' + line)

            i += 1
        if code != 0:
            exit(1)
    print()
