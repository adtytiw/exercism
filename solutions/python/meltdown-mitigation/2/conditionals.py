"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    
    # All three conditions must be True for the reactor to be balanced.
    return (temperature < 800 
            and neutrons_emitted > 500 
            and (temperature * neutrons_emitted < 500000))


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power) * 100

    # Using guard clauses: if a condition is met, return and exit.
    # This removes the need for 'elif' or 'else'.
    
    if percentage_value >= 80:
        return "green"
    
    # If we're here, we know percentage_value < 80
    if percentage_value >= 60:
        return "orange"
        
    # If we're here, we know percentage_value < 60
    if percentage_value >= 30:
        return "red"
        
    # If none of the above, it must be < 30
    return "black"
    


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    product = temperature * neutrons_produced_per_second
    
    # Calculate the bounds based on the threshold
    low_bound = 0.9 * threshold
    high_bound = 1.1 * threshold

    # Use guard clauses for 'LOW' and 'NORMAL'
    
    # 1. Check if the product is below the 90% mark
    if product < low_bound:
        return "LOW"
    
    # 2. Check if the product is within the 90% - 110% range (inclusive)
    #    We only check this if the 'LOW' condition was false.
    if low_bound <= product <= high_bound:
        return "NORMAL"
        
    # 3. If it's not 'LOW' and not 'NORMAL', it must be 'DANGER'
    return "DANGER"