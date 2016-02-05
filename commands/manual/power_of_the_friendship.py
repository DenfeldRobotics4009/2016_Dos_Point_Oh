__author__ = "nikolojedison"

from wpilib.command import Command

class DriveWithJoystick(Command):

    def __init__(self, robot):
        """Initialise the DriveWithJoystick command."""

        super().__init__()
        self.robot = robot
        self.requires(self.robot.drivetrain)

    def execute(self):
        """Pass the joystick values directly to the driveJoystick function."""
        self.robot.drivetrain.driveJoystick(self.robot.oi.getStick())

    def isFinished(self):
        """Code that runs when isFinished is called."""
        #keep the robot from running the driveJoystick command once then dying:
        return False

    def end(self):
        """Code that runs when end is called."""

        #Set the drivetrain values to 0 so the robot stops:
        self.robot.drivetrain.driveManual(0,0)
        pass

    def interrupted(self):
        """Code that runs when the command is interrupted."""
        #If interrupted (could do logs here):
        self.end()
