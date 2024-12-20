#vessel hydrodynamics project

G = 9.81
#gravitational acceleration equal to meter per square second
METER_PER_FEET = 0.3
KNOT_PER_METER_SEC = 0.51

def get_color():
    """
    This function takes an input from the user, which is a string value
    corresponding to a color.
    
    Parameters:
    None
    
    Returns:
    color (str): The number corresponding to the color of the vessel as input by the
    user
    
    Example:
    -- get_color()
    Select which number correponds to the color of your vessel
    1 - Red
    2 - Blue 
    3 - White 
    What is the color of your vessel? 2
    '2'  
    -- get_color()
    Select which number correponds to the color of your vessel
    1 - Red
    2 - Blue 
    3 - White 
    What is the color of your vessel? abc
    ERROR: The value you selected does not correspond to a color
    Please choose another number between 1 and 3: 
    -- get_color()
    Select which number correponds to the color of your vessel
    1 - Red
    2 - Blue 
    3 - White 
    What is the color of your vessel? 1.7
    ERROR: The value you selected does not correspond to a color
    Please choose another number between 1 and 3:    
    """
    color = input('Select which number corresponds to the color of your'\
                  ' vessel\n1-Red\n2-Blue \n3-White \nWhat is the color'\
                  ' of your vessel? ')
    while is_valid_text(color,'1','3') == False or 3 < float(color)\
    or 1 > float(color):
        print('ERROR: The value you selected does not correspond'\
        ' to a color')
        color = input('Please choose another number between 1 and 3: ')
    else:
        return color

def ship_or_boat():
    """
    Takes input from user, returns string value of either 'Boat' or 'Ship'.
    
    Parameters:
    None
    
    Returns:
    str: Either 'Boat' or 'Ship' depending on weight entered by user.
    
    Example:
    -- ship_or_boat()
    Please enter the weight of your vessel in Tons: 412
    'Boat'
    -- ship_or_boat()
    Please enter the weight of your vessel in Tons: 1200
    'Ship'
    -- ship_or_boat()
    Please enter the weight of your vessel in Tons: 500
    'Ship'
    """
    weight = float(input('Please enter the weight of your vessel in Tons: '))
    if weight < 500:
        return 'Boat'
    else:
        return 'Ship'

def feet_to_meter(feet):
    """
    Converts and returns a value in feet to meters, rounded to 2 decimal
    places.
    
    Parameters:
    float: Positive float value representing a length in feet
    
    Returns:
    float: Computed value converted from feet to meters rounded to 2 decimal
    places
    
    Example:
    -- feet_to_meter(1)
    0.3
    -- feet_to_meter(2.5)
    0.75
    -- feet_to_meter(100)
    30
    """
    meters = round(feet * METER_PER_FEET,2)
    return meters

def knot_to_meter_sec(knots):
    """
    Converts and returns a value in knots to meters per second, rounded
    to 2 decimal places.
    
    Parameters:
    float: Positive float value representing a velocity in knots
    
    Returns:
    float: Computed value converted from knots to meters per second rounded
    to 2 decimal places
    
    Example:
    -- knot_to_meter_sec(2.6)
    1.33
    -- knot_to_meter_sec(100)
    51.0
    -- knot_to_meter_sec(1)
    0.51
    """
    mps = round(knots * KNOT_PER_METER_SEC,2)
    #mps = meters per second
    return mps

def is_positive(x):
    """
    Takes a number value and verifies whether or not that number is positive.
    
    Parameters:
    x (num): Takes a number value.
    
    Returns:
    bool: Returns a boolean value signifying whether or not the number
    is positive.
    
    Example:
    -- is_positive(100)
    True
    -- is_positive(-6)
    False
    -- is_positive(1)
    True
    """
    if x > 0:
        return True
    else:
        return False
    
def compute_froude(feet,knots):
    """
    Takes two float values to compute and return the Froude number.
    
    Parameters:
    feet (float): Float value representing a length in feet.
    knots (float): Float value representing velocity in knots.
    
    Returns:
    froude (float): Computed Froude number
    
    Example:
    -- compute_froude(2.5,6)
    1.13
    -- compute_froude(350,198)
    3.15
    -- compute_froude(200,41)
    0.86
    """
    velocity_ms = knot_to_meter_sec(knots)
    length = feet_to_meter(feet)
    froude = (velocity_ms) / (length * G) ** (1/2)
    froude = round(froude,2)
    return froude

def display_hydro_lift(feet,knots):
    """
    Void function that takes two float values of feet and knots and computes
    the Froude number, then determines hydrodynamic lift.
    
    Parameters:
    float: Positive float value representing a length in feet.
    float: Positive float value representing velocity in knots.
    
    Returns:
    None
    
    Example:
    -- display_hydro_lift(8,5)
    Negative hydrodynamic lift
    -- display_hydro_lift(10,0)
    Negligible hydrodynamic lift compared to Archimedes thrust
    -- display_hydro_lift(5,10)
    Hydrodynamic lift represents 50% of the displacement
    """
    hydrolift = compute_froude(feet,knots)
    if hydrolift < 0.3:
        print('Negligible hydrodynamic lift compared to Archimedes thrust')
    elif hydrolift >= 0.3 and hydrolift < 0.7:
        print('Negative hydrodynamic lift')
    else:
        print('Hydrodynamic lift represents 50% of the displacement')

def is_valid_text(text,string_min,string_max):
    """
    Function takes 3 inputs and returns a boolean variable to measure
    if the first input falls in between the range of the second and third
    inputs.
    
    Parameters:
    text (str): Input to be checked for validity
    string_min (str): Lower bound character to check for validity of input
    string_max (str): Upper bound character to check for validity of input
    
    Returns:
    bool: A boolean variable verifying that the input string is either valid
    or invalid, represented by True or False, respectively.
    
    Example:
    -- is_valid_text('jvi','a','z')
    True
    -- is_valid_text('345','b','r')
    False
    -- is_valid_text('33','1','3')
    True
    """
    is_valid = True
    for ch in text:
        if ord(ch) < ord(string_min) or ord(ch) > ord(string_max):
            is_valid = False
    return is_valid

def vessel_program():
    """
    Void function that gathers information on vessel from user, and then
    given that information computes Froude number and tells user about
    hydrodynamic lift of the vessel.
    
    Parameters:
    None
    
    Returns:
    None
    """
    print('**** WELCOME TO THE SHIP SCIENCE PROGRAM! ****')
    color = get_color()
    print('You selected color number:',color)
    vessel_type = ship_or_boat()
    length = float(input('What is the length of the ' + str(vessel_type) + \
                         ' in feet? '))
    positive = is_positive(length)
    if positive == True:
        velocity = float(input('What is the speed of the '\
                               + str(vessel_type) + ' in knot? : '))
        hydro_lift = display_hydro_lift(length,velocity)
    else:
        print('It is impossible to compute Froude number since the length'\
              ' is less than or equal to 0')
    print('**** END OF THE PROGRAM. GOODBYE! ****')
