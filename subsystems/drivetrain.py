__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem
from commands.manual.mecanum_drive_with_joystick import MecanumDriveWithJoystick
from utilities.drive_control import *

class Drivetrain(Subsystem):
    '''Class drivetrain uses a few Talons to run a 'bot.
    '''

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.drive = wpilib.RobotDrive(DriveMotor(0), DriveMotor(2), DriveMotor(1), DriveMotor(3))
        self.drive.setExpiration(0.1)

        self.drive.setInvertedMotor(self.drive.MotorType.kFrontRight, True)
        self.drive.setInvertedMotor(self.drive.MotorType.kRearRight, True)

        self.x = 0
        self.y = 0
        self.rotation = 0


    def initDefaultCommand(self):
        '''When no other command is running let the operator drive around
           using the joystick'''
        self.setDefaultCommand(MecanumDriveWithJoystick(self.robot))

    def log(self):
        pass

    def driveJoystick(self, joystick):
        precision = True
        x = joystick.getX()
        y = joystick.getY()
        z = joystick.getRawAxis(3)
        if x>1:
            x=1
        elif x<-1:
            x=-1
        self.driveManual(x,y,z)

    def driveManual(self, x, y , rotation):
        self.x, self.y, self.rotation = x, y, rotation
        self.drive.mecanumDrive_Cartesian(x, y, rotation, 0)
