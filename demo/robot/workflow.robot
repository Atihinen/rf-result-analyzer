*** Settings ***
Library    TrafficLibrary
Test Setup    Power On System

*** Variables ***
${TIMER_INTERVAL}    30s
${PRESSURE_SENSOR_TIMEOUT}    10s
${USB_SERIAL_PORT}    /dev/ttyUSB0

*** Test Cases ***
Test Timer Trigger for Traffic Lights
    [Documentation]    Verify the timer trigger functionality for traffic lights.
    Set Timer    ${TIMER_INTERVAL}
    Wait For Timer    ${TIMER_INTERVAL}
    Verify Traffic Light Sequence

Test Pressure Sensor Trigger for Traffic Lights
    [Documentation]    Verify the pressure sensor trigger functionality for traffic lights.
    Verify Pressure Sensor
    Simulate Vehicle Detection
    Verify Traffic Light Change For Vehicle

Test Maintenance Connection Trigger for Traffic Lights
    [Documentation]    Verify the maintenance connection trigger functionality for traffic lights.
    Connect Maintenance Device    ${USB_SERIAL_PORT}
    Initiate Maintenance Connection
    Verify Maintenance Mode
    Perform Maintenance Operations

*** Keywords ***
Power On System
    TrafficLibrary.Power On System

Set Timer
    [Arguments]    ${interval}
    TrafficLibrary.Set Timer    ${interval}

Wait For Timer
    [Arguments]    ${interval}
    TrafficLibrary.Wait For Timer    ${interval}

Verify Traffic Light Sequence
    TrafficLibrary.Verify Traffic Light Sequence

Verify Pressure Sensor
    TrafficLibrary.Verify Pressure Sensor

Simulate Vehicle Detection
    TrafficLibrary.Simulate Vehicle Detection

Verify Traffic Light Change For Vehicle
    TrafficLibrary.Verify Traffic Light Change For Vehicle

Connect Maintenance Device
    [Arguments]    ${port}
    TrafficLibrary.Connect Maintenance Device    ${port}

Initiate Maintenance Connection
    TrafficLibrary.Initiate Maintenance Connection

Verify Maintenance Mode
    TrafficLibrary.Verify Maintenance Mode

Perform Maintenance Operations
    TrafficLibrary.Perform Maintenance Operations

Verify Arduino Uno Setup
    TrafficLibrary.Verify Arduino Uno Setup

Initiate Setup Process
    TrafficLibrary.Initiate Setup Process

Verify System Configuration
    TrafficLibrary.Verify System Configuration

Verify System Operation
    TrafficLibrary.Verify System Operation
    *** Test Setup ***
    Power On System