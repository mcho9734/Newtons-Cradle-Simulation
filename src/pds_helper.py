import pandas as pd
from typing import Any
from support.constants import NC_FP

def extract_and_convert(relative_filepath:str)-> list[dict[str, Any]]:
    """
    Creates a list of pendula given a CSV file.

    Args:
        relative_filepath (str): filepath to access CSV with pendula data

    Returns:
        (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    
    """
    df = pd.read_csv(relative_filepath) 
    bad_rep = df.to_dict(orient="index") 

    # TODO 0: Fix the bad representation
    ...


# Provided
def write_to_csv(pend_list):
    """
    Writes a pend_list to the Newton's Cradle CSV file called "newton_cradle_pends.csv"

    Args:
        pend_list (list[dict]): list of dictionaries, each dictionary corresponding to
        a pendulum, with keys as physical attributes
    """
    df = pd.DataFrame.from_dict(pend_list)
    df.to_csv(NC_FP, index=False)  