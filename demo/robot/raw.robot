*** Settings ***
Library    TrafficLibrary

*** Variables ***
${USB_SERIAL_PORT}    /dev/ttyUSB0
${TIMER_INTERVAL}    10s
${GREEN_LIGHT}    0
${PRESSURE_SENSOR_PIN}    A0
${PRESSURE_SENSOR_VALUE}    100

*** Test Cases ***
Timer Trigger for Traffic Lights
    Connect To System    ${USB_SERIAL_PORT}
    Wait Until ACK
    Set Timer    ${TIMER_INTERVAL}
    Wait Until Keyword Succeeds   30s    2s    IO Status Should Be    ${GREEN_LIGHT}    ${True}

Pressure Sensor Trigger for Traffic Lights
    Connect To System    ${USB_SERIAL_PORT}
    Wait Until ACK
    Analog Value Should Be   ${PRESSURE_SENSOR_PIN}    0
    Set Analog Value    ${PRESSURE_SENSOR_PIN}    ${PRESSURE_SENSOR_VALUE}
    Wait Until Keyword Succeeds   30s    2s    IO Status Should Be    ${GREEN_LIGHT}    ${True}

Maintenance Connection Trigger for Traffic Lights
    Connect To System    ${USB_SERIAL_PORT}
    Wait Until ACK
    Run Serial Command    MP    ${0x01}
    Serial Value Should Be    ${0x02}
    Run Serial Command    GRT
    Wait Until Keyword Succeeds   30s    2s    IO Status Should Be    ${GREEN_LIGHT}    ${True}
