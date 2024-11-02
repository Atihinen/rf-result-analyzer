import random
from robot.api import logger
            

class TrafficLibrary():
    def __init__(self, level="plain"):
        self.level = level
    
    def _random_exception(self, error_messages):
        if random.random() < 0.3:
            if self.level == "plain":
                raise Exception("Timeout")
            else:
                raise Exception(random.choice(error_messages))

    def power_on(self):
        error_messages = [
            "GPIO input error: Unable to set power on",
            "GPIO input error: Power on signal not received",
            "GPIO input error: Device not responding to power on command"
        ]
        self._random_exception(error_messages)
        logger.info("Powering on the device")
    
    def set_timer(self, seconds):
        error_messages = [
            "GPIO input error: Unable to set timer",
            "GPIO input error: Timer signal not received",
            "GPIO input error: Device not responding to timer command"
        ]
        self._random_exception(error_messages)
        logger.info(f"Setting timer to {seconds} seconds")
    
    def verify_traffic_light_sequence(self):
        error_messages = [
            "Serial port error: Unable to verify traffic light sequence",
            "Serial port error: Traffic light sequence data corrupted",
            "Serial port error: No response from traffic light controller"
        ]
        self._random_exception(error_messages)
        logger.info("Verifying the traffic light sequence")
    
    def verify_sensor(self, pin):
        error_messages = [
            "GPIO input error: Unable to verify sensor",
            "GPIO input error: Sensor signal not received",
            "GPIO input error: Device not responding to sensor verification command"
        ]
        self._random_exception(error_messages)
        logger.info(f"Verifying sensor on pin {pin}")
    
    def simulate_sensor_trigger(self, pin):
        error_messages = [
            "GPIO input error: Unable to simulate sensor trigger",
            "GPIO input error: Sensor trigger signal not received",
            "GPIO input error: Device not responding to sensor trigger command"
        ]
        self._random_exception(error_messages)
        logger.info(f"Simulating sensor trigger on pin {pin}")
    
    def verify_traffic_light_change_for_vehicle(self):
        error_messages = [
            "Traffic light error: Unable to verify light change for vehicle",
            "Traffic light error: Light change signal not received for vehicle",
            "Traffic light error: Vehicle detection failed during light change verification"
        ]
        self._random_exception(error_messages)
        logger.info("Verifying traffic light change for vehicle")
    
    def open_connection(self, port):
        error_messages = [
            "Serial port error: Unable to open connection",
            "Serial port error: Connection timeout",
            "Serial port error: Port not found or inaccessible"
        ]
        self._random_exception(error_messages)
        logger.info(f"Opening connection to port {port}")

    def write(self, cmd):
        error_messages = [
            "Serial port error: Command write failed",
            "Serial port error: Command not acknowledged",
            "Serial port error: Device not responding to write command"
        ]
        self._random_exception(error_messages)
        logger.info(f"Writing command {cmd}")
    
    def read_until_(self, mode):
        error_messages = [
            "Serial port error: Read timeout",
            "Serial port error: Data corrupted during read",
            "Serial port error: No data received from device"
        ]
        self._random_exception(error_messages)
        logger.info(f"Reading until {mode}")
    
    def connect_to_system(self, port):
        error_messages = [
            "SPI error: Unable to establish connection",
            "SPI error: Connection timeout",
            "SPI error: Device not responding to SPI commands"
        ]
        self._random_exception(error_messages)
        self.open_connection(port)
    
    def set_timer(self, pin):
        error_messages = [
            "GPIO input error: Unable to set timer",
            "GPIO input error: Timer signal not received",
            "GPIO input error: Device not responding to timer command"
        ]
        self._random_exception(error_messages)
        self.write(f"SET_TIMER {pin}")
    
    def wait_until_ack(self):
        error_messages = [
            "Serial port error: ACK not received",
            "Serial port error: ACK signal corrupted",
            "Serial port error: Timeout while waiting for ACK"
        ]
        self._random_exception(error_messages)
        self.read_until_("ACK")
    
    def set_analog_value(self, pin, value):
        error_messages = [
            "Analog-to-Digital Converter (ADC) error: Unable to read analog value",
            "Analog-to-Digital Converter (ADC) error: Analog value read timeout",
            "Analog-to-Digital Converter (ADC) error: Data corrupted during analog value read"
        ]
        self._random_exception(error_messages)
        self.write(f"SET_ANALOG_VALUE {pin} {value}")
    
    def analog_value_should_be(self, pin, value):
        error_messages = [
            "Analog-to-Digital Converter (ADC) error: Analog value mismatch",
            "Analog-to-Digital Converter (ADC) error: Analog value read timeout",
            "Analog-to-Digital Converter (ADC) error: Data corrupted during analog value read"
        ]
        self._random_exception(error_messages)
        self.write(f"GET_ANALOG_VALUE {pin}")
        self.read_until_(f"ANALOG_VALUE {pin} {value}")
    
    def run_serial_command(self, cmd, value=0):
        error_messages = [
            "Serial command error: Command execution failed",
            "Serial command error: Command not recognized",
            "Serial command error: Device not responding to serial command"
        ]
        self._random_exception(error_messages)
        self.write(cmd)
        self.wait_until_ack()
    
    def serial_value_should_be(self, value=0):
        error_messages = [
            "Serial command error: Value mismatch",
            "Serial command error: Value read timeout",
            "Serial command error: Data corrupted during value read"
        ]
        self._random_exception(error_messages)
        self.read_until_(value)
    
    def power_on_system(self):
        error_messages = [
            "Serial command error: Unable to send power on command",
            "Serial command error: Power on command not acknowledged",
            "Serial command error: Device not responding to power on command"
        ]
        self._random_exception(error_messages)
        self.power_on()
    
    def verify_pressure_sensor(self):
        error_messages = [
            "Pressure sensor error: Unable to verify pressure sensor",
            "Pressure sensor error: Pressure sensor data corrupted",
            "Pressure sensor error: No response from pressure sensor"
        ]
        self._random_exception(error_messages)
        logger.info("Verifying pressure sensor")
    
    def wait_for_timer(self, seconds):
        error_messages = [
            "I2C error: Unable to read timer value",
            "I2C error: Timer read signal not received",
            "I2C error: Device not responding to timer read command"
        ]
        self._random_exception(error_messages)
        self.set_timer(seconds)
        self.wait_until_ack()
    
    def simulate_vehicle_detection(self):
        error_messages = [
            "Simulation error: Unable to trigger vehicle detection",
            "Simulation error: Vehicle detection signal not received",
            "Simulation error: Device not responding to vehicle detection simulation"
        ]
        self._random_exception(error_messages)
        self.simulate_sensor_trigger(1)
    
    def connect_maintenance_device(self, port):
        error_messages = [
            "SPI error: Unable to establish maintenance connection",
            "SPI error: Connection timeout",
            "SPI error: Device not responding to maintenance commands"
        ]
        self._random_exception(error_messages)
        self.connect_to_system(port)
    
    def initiate_maintenance_connection(self):
        error_messages = [
            "SPI error: Unable to initiate maintenance connection",
            "SPI error: Connection timeout",
            "SPI error: Device not responding to maintenance initiation command"
        ]
        self._random_exception(error_messages)
        self.connect_maintenance_device(1)
    
    def verify_maintenance_mode(self):
        error_messages = [
            "Maintenance mode error: Unable to verify maintenance mode",
            "Maintenance mode error: Maintenance mode data corrupted",
            "Maintenance mode error: No response from maintenance controller"
        ]
        self._random_exception(error_messages)
        logger.info("Verifying maintenance mode")
    
    def perform_maintenance_operations(self):
        error_messages = [
            "Maintenance mode error: Unable to perform maintenance operations",
            "Maintenance mode error: Maintenance operations failed",
            "Maintenance mode error: Device not responding to maintenance operations command"
        ]
        self._random_exception(error_messages)
        logger.info("Performing maintenance operations")
    
    def io_status_should_be(self, pin, value):
        error_messages = [
            "GPIO input error: IO status mismatch",
            "GPIO input error: IO status read timeout",
            "GPIO input error: Data corrupted during IO status read"
        ]
        self._random_exception(error_messages)
        logger.info(f"IO status should be {value} on pin {pin}")
