__author__ = "nikolojedison & auxchar"
#Code copied from 2015_Lopez_Jr. Some changes to fit with 2016 setup.

import wpilib

from utilities.settings import Settings

def precision_mode(controller_input, trigger, button):
    """copied from CubertPy and tweaked for 2016 use."""

    if trigger == True and not button == True:
        #if the trigger is pulled, use the first precision:
        return controller_input * Settings.num_precision_one
    elif button == True and not trigger == True:
        #if the thumb button is held, use the second precision:
        return controller_input * Settings.num_precision_two
    elif button == True and trigger == True:
        #if both are held, use the combined precision (or a third, separate precision):
        return controller_input * Settings.num_precision_one * Settings.num_precision_two
    else:
        #if none are held, just return straight controller_input:
        return controller_input

def inverse_dead_zone(motor_output, dead_zone):
    """This is the inverted dead zone code which is important for Talons."""
    if abs(motor_output) < .00001: #floating point rounding error workaround.
        return 0
    elif motor_output > 0:
        return (motor_output*(1-dead_zone))+dead_zone
    else:
        return (-motor_output*(dead_zone-1))-dead_zone

def exponential_scaling(base, exponent):
    """Behold, exponents that don't die with negative values."""

    if base>0:
        return abs(base)**exponent
    else:
        return -(abs(base)**exponent)

def dead_zone(controller_input, dead_zone):
    """Old-style dead zone scaling. Will likely be removed."""

    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        return ((controller_input-dead_zone)/(1-dead_zone))
    else:
        return ((-controller_input-dead_zone)/(dead_zone-1))

class DriveMotor(wpilib.Talon):
    """A motor controller that overcomes static friction."""
    def set(self, speed, syncGroup=0):
        super().set(inverse_dead_zone(speed, .1),syncGroup=syncGroup)

def drive_control(controller_input, trigger, button):
    """Final y-axis thing that's used by the drivetrain class."""

    return precision_mode(exponential_scaling(exponential_scaling(dead_zone(controller_input, 0.5), 0.5)*0.5, 1.1), trigger, button)

def twist_control(controller_input, trigger, button):
    """Final spin thing that's used by the drivetrain class."""

    return precision_mode(exponential_scaling(exponential_scaling(controller_input, 0.5)*0.5, 2.3), trigger, button)
