*** Settings ***
Resource    library.resource
Library           Collections

*** Variables ***
${TIMER_INTERVAL}    10s
${PRESSURE_SENSOR_PIN}    A0
${USB_SERIAL_PORT}    /dev/ttyUSB0

*** Test Cases ***

Timer Trigger for Traffic Lights
    [Documentation]    The system should change the traffic lights based on a predefined timer.
    Given the system is powered on
    And the timer is set to ${TIMER_INTERVAL}
    When the timer reaches the predefined interval
    Then the system changes the traffic lights according to the sequence

Pressure Sensor Trigger for Traffic Lights
    [Documentation]    The system should change the traffic lights based on input from a pressure sensor.
    Given the system is powered on
    And the pressure sensor is functional
    When the pressure sensor detects a vehicle
    Then the system changes the traffic lights to allow the vehicle to pass

Maintenance Connection Trigger for Traffic Lights
    [Documentation]    The system should allow maintenance operations via a USB serial connection.
    Given the system is powered on
    And connected to a maintenance device via USB
    When maintenance personnel initiate a connection via USB serial
    Then the system enters maintenance mode
    And maintenance personnel perform necessary operations

*** Keywords ***

The system is powered on
    [Documentation]    Ensure the system is powered on.
    TrafficLibrary.Power On

The timer is set to ${interval}
    [Documentation]    Set the timer to the specified interval.
    TrafficLibrary.Set Timer    ${interval}

The timer reaches the predefined interval
    [Documentation]    Wait for the timer to reach the predefined interval.
    Sleep    ${TIMER_INTERVAL}

The system changes the traffic lights according to the sequence
    [Documentation]    Verify the traffic lights change according to the sequence.
    TrafficLibrary.Verify Traffic Light Sequence

The pressure sensor is functional
    [Documentation]    Ensure the pressure sensor is functional.
    TrafficLibrary.Verify Sensor    ${PRESSURE_SENSOR_PIN}

The pressure sensor detects a vehicle
    [Documentation]    Simulate vehicle detection by the pressure sensor.
    TrafficLibrary.Simulate Sensor Trigger    ${PRESSURE_SENSOR_PIN}

The system changes the traffic lights to allow the vehicle to pass
    [Documentation]    Verify the traffic lights change to allow the vehicle to pass.
    TrafficLibrary.Verify Traffic Light Change For Vehicle

Connected to a maintenance device via USB
    [Documentation]    Ensure the system is connected to a maintenance device via USB.
    TrafficLibrary.Open Connection    ${USB_SERIAL_PORT}

Maintenance personnel initiate a connection via USB serial
    [Documentation]    Simulate maintenance personnel initiating a connection via USB serial.
    TrafficLibrary.Write    CONNECT

The system enters maintenance mode
    [Documentation]    Verify the system enters maintenance mode.
    TrafficLibrary.Read Until    MAINTENANCE MODE

Maintenance personnel perform necessary operations
    [Documentation]    Simulate maintenance operations.
    TrafficLibrary.Write    PERFORM MAINTENANCE

The Arduino Uno and necessary components are available
    [Documentation]    Ensure the Arduino Uno and necessary components are available.
    TrafficLibrary.Verify Components

The system installer initiates the setup process
    [Documentation]    Simulate the system installer initiating the setup process.
    Log    Initiating setup process

The system installer connects the Arduino Uno and other components
    [Documentation]    Simulate connecting the Arduino Uno and other components.
    TrafficLibrary.Connect Components

The system is powered on and configured for the demo environment
    [Documentation]    Power on and configure the system for the demo environment.
    TrafficLibrary.Configure For Demo

The system operates as expected in the demo environment
    [Documentation]    Verify the system operates as expected in the demo environment.
    TrafficLibrary.Verify Demo Operation
