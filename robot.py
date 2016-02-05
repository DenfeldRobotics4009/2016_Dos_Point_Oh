#!/usr/bin/env python3
__author__ = "nikolojedison"

#Import robot-specific libraries:
import wpilib
from wpilib.command import Scheduler
import networktables

#Import our robot-specific libraries:
from utilities.settings import Settings

#Import our subsystems:
from subsystems.drivetrain import Drivetrain

#Import our button mapping:
from oi import OI

class Mantis(wpilib.SampleRobot):
    """Fluffy ears to scratch, lost his tail, cute little paws, likes to play fetch."""

    def robotInit(self):
        """Initialise the robot."""

        #Initialise the subsystems and the button mapping:
        self.drivetrain = Drivetrain(self)
        self.oi = OI(self)

        #Timeout value for the macros from the dashboard (default 15 sec).
        self.macroTimeout = self.oi.smart_dashboard.getInt("Macro", 15)
        Settings.num_macro_timeout = self.macroTimeout

        #these are all actually really self explanatory. Wonder if they work.
        self.camera = wpilib.USBCamera()
        self.camera.setExposureManual(50)
        self.camera.setBrightness(80)
        self.camera.setFPS(15)
        self.camera.setSize(320, 240)
        self.camera.setWhiteBalanceAuto()
        self.camera.updateSettings() #update with the new settings so it actually does what we want it to

        server = wpilib.CameraServer.getInstance() #set up the camera server
        server.startAutomaticCapture(self.camera) #start the camera server

    def autonomous(self):
        """Auton code."""

        #Logging loop
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def operatorControl(self):
        """Teleop code."""
        #Make the joystick work for driving:
        joystick = self.oi.getStick()

        #Logging loop
        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def disabled(self):
        """Code to run when disabled."""

        #Stop the drivetrain for safety's sake:
        self.drivetrain.driveManual(0,0,0)

        #Logging loop
        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def test(self):
        """Code for testing."""
        pass

    def log(self):
        """I know it doesn't log but if it does eventually it'll go here."""
        #Log the things:
        self.drivetrain.log()

if __name__ == "__main__":
    wpilib.run(Mantis)
