__author__ = "nikolojedison"

import wpilib
from wpilib.buttons import JoystickButton, InternalButton
from networktables import NetworkTable

from utilities.pov_button import POVButton
from utilities.drive_control import *
from utilities.settings import Settings

from macros.play_macro import PlayMacro
from macros.record_macro import RecordMacro

class OI:
    """Button mapping goes here."""

    def __init__(self, robot):
        """This is assuming that the joystick used is the Logitech Extreme 3D."""

        #initialise the stick and the smart dashboard (in case we need stuff for auton):
        self.stick = wpilib.Joystick(0)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Main stick buttons.
        #-----------------------------------------------------------------------
        trigger = JoystickButton(self.stick, 1)
        thumb = JoystickButton(self.stick, 2)
        bottom_left = JoystickButton(self.stick, 3)
        bottom_right = JoystickButton(self.stick, 4)
        top_left = JoystickButton(self.stick, 5)
        top_right = JoystickButton(self.stick, 6)


        #Goes from front to back. outer_base is the outer ring of buttons on
        #the base, inner_base is the inner ring of buttons on the base.
        #-----------------------------------------------------------------------
        outer_base_one = JoystickButton(self.stick, 7)
        inner_base_one = JoystickButton(self.stick, 8)
        outer_base_two = JoystickButton(self.stick, 9)
        inner_base_two = JoystickButton(self.stick, 10)
        outer_base_three = JoystickButton(self.stick, 11)
        inner_base_three = JoystickButton(self.stick, 12)

        #Hat switch POV stuff.
        #-----------------------------------------------------------------------
        pov_north = POVButton(self.stick, 0)
        pov_northeast = POVButton(self.stick, 45)
        pov_east = POVButton(self.stick, 90)
        pov_southeast = POVButton(self.stick, 135)
        pov_south = POVButton(self.stick, 180)
        pov_southwest = POVButton(self.stick, 225)
        pov_west = POVButton(self.stick, 270)
        pov_northwest = POVButton(self.stick, 315)

    def getStick(self):
        """Drive joystick."""
        return self.stick
