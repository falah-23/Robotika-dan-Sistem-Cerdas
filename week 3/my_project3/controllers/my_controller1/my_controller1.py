from controller import Robot

robot = Robot()

timeStep = 64

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

speed = 5

leftMotor.setVelocity(speed)
rightMotor.setVelocity(speed)

while robot.step(timeStep) != -1:
    pass
