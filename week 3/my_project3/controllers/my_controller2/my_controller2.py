from controller import Robot

robot = Robot()

timeStep = 64

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftSpeed = 2.5
rightSpeed = 5

leftMotor.setVelocity(leftSpeed)
rightMotor.setVelocity(rightSpeed)

while robot.step(timeStep) != -1:
    pass
