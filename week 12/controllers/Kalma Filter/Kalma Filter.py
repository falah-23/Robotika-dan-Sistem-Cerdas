from controller import Robot, Motor, DistanceSensor
import numpy as np

class EPuck:
    def __init__(self):
        self.robot = Robot()
        self.time_step = int(self.robot.getBasicTimeStep())

        # Motors
        self.left_motor = self.robot.getDevice('left wheel motor')
        self.right_motor = self.robot.getDevice('right wheel motor')
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        self.left_motor.setVelocity(0)
        self.right_motor.setVelocity(0)

        # Encoders
        self.left_encoder = self.robot.getDevice('left wheel sensor')
        self.right_encoder = self.robot.getDevice('right wheel sensor')
        self.left_encoder.enable(self.time_step)
        self.right_encoder.enable(self.time_step)

        # Distance Sensors
        self.sensors = []
        self.sensor_names = [
            'ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7'
        ]
        for name in self.sensor_names:
            sensor = self.robot.getDevice(name)
            sensor.enable(self.time_step)
            self.sensors.append(sensor)

        # Kalman Filter State
        self.state = np.array([0, 0, 0])  # [x, y, theta]
        self.covariance = np.eye(3) * 0.1
        self.process_noise = np.eye(3) * 0.01
        self.measurement_noise = np.eye(3) * 0.1

    def read_sensors(self):
        return [sensor.getValue() for sensor in self.sensors]

    def kalman_predict(self, control):
        # Unpack control inputs
        velocity, angular_velocity = control
        dt = self.time_step / 1000.0

        # State transition model
        theta = self.state[2]
        A = np.array([
            [1, 0, -velocity * np.sin(theta) * dt],
            [0, 1, velocity * np.cos(theta) * dt],
            [0, 0, 1]
        ])

        # Control model
        B = np.array([
            [np.cos(theta) * dt, 0],
            [np.sin(theta) * dt, 0],
            [0, dt]
        ])

        # Predict state and covariance
        self.state = A @ self.state + B @ np.array(control)
        self.covariance = A @ self.covariance @ A.T + self.process_noise

    def kalman_update(self, measurement):
        # Measurement model
        H = np.eye(3)

        # Kalman gain
        S = H @ self.covariance @ H.T + self.measurement_noise
        K = self.covariance @ H.T @ np.linalg.inv(S)

        # Update state and covariance
        y = measurement - H @ self.state
        self.state += K @ y
        self.covariance = (np.eye(3) - K @ H) @ self.covariance

    def set_motor_velocity(self, left_speed, right_speed):
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)

    def main_loop(self):
        while self.robot.step(self.time_step) != -1:
            # Read sensor data
            sensor_values = self.read_sensors()

            # Example control input: move forward
            control = [2, 0]  # [velocity, angular_velocity] (increased speed)

            # Kalman Filter Prediction
            self.kalman_predict(control)

            # Example measurement from sensors (mocked)
            measurement = self.state + np.random.normal(0, 0.1, size=3)

            # Kalman Filter Update
            self.kalman_update(measurement)

            # Set motor speeds
            left_speed = control[0] - control[1]
            right_speed = control[0] + control[1]
            self.set_motor_velocity(left_speed, right_speed)

            # Print Kalman Filter state
            print(f"Kalman Filter State: x={self.state[0]:.2f}, y={self.state[1]:.2f}, theta={self.state[2]:.2f}")

if __name__ == "__main__":
    epuck = EPuck()
    epuck.main_loop()
