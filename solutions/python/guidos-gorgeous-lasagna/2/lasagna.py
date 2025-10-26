"""
This module contains functions to calculate the preparation and
baking times for a lasagna.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes."""
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total elapsed time in minutes."""
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time