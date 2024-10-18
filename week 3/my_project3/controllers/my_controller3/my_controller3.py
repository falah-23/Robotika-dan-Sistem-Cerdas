from controller import Robot

robot = Robot()

timeStep = 64

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

proxSensors = []
for i in range(8):
    proxSensors.append(robot.getDevice('ps0'))
    proxSensors[i].enable(timeStep)

speed = 6.28
leftMotor.setVelocity(speed)
rightMotor.setVelocity(speed)

while robot.step(timeStep) != -1:
    frontProxValue = proxSensors[0].getValue()

    if frontProxValue > 80:
        leftMotor.setVelocity(0)
        rightMotor.setVelocity(0)
    else:
        leftMotor.setVelocity(speed)
        rightMotor.setVelocity(speed)
