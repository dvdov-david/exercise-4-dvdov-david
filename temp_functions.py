"""
Script to handle temperatures in celsius degrees and classify them

Usage:
    ./temp_functions.py
    
Author:
    David O. - 02/12/2020
    
License:
    Creative commons
"""


def fahr_to_celsius(temp_fahrenheit):
    """
    Function for getting temperature in Celsius from Fahrenheit.

    Parameters
    ----------
    temp_fahrenheit: Temperature in temp_fahrenheit 
                     <numerical>

    Returns
    -------
    coverted_temp: Temperature in Celsius
                   <float>
        
    """
 
    converted_temp = (temp_fahrenheit - 32)/1.8
    return converted_temp



def temp_classifier(temp_celsius):
    """
    Function to reclassify temperature(celsius degree) in one of 4 categories
    
    Parameters
    ----------
    temp_celsius: Temperature in celsius degree 
                  <numerical>

    Returns
    -------
    reclass_temp: category of temperature(0,1,2,3)
                   <float>
        
    """
    
    if temp_celsius < -2:
        reclass_temp = 0
    elif temp_celsius >=-2 and temp_celsius < 2:
        reclass_temp = 1
    elif temp_celsius >=2 and temp_celsius < 15:
        reclass_temp = 2
    else:
        reclass_temp = 3
    
    return reclass_temp