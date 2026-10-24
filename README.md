# Andon-Project
Project Working on python (PYQT5)


Project Title: HELP CHAIN ANDON System
1. Short Project Description
The HELP CHAIN ANDON System is a Python-based desktop application developed using PyQt5. It provides a graphical interface with four help-request buttons: Production, Maintenance, Quality, and Tool.

Each department has a circular LED indicator. When an operator clicks a button, the corresponding LED changes color in sequence: Green → Red → Yellow → Green. This provides a simple visual indication of the department's help-request status.

The application uses the QLed library for LED indicators and PyQt5 widgets for the user interface. It can serve as a basic prototype for an industrial help-request or Andon monitoring system.
2. Main Modules
Module	Description
Production	Displays the production help-request indicator.
Maintenance	Displays the maintenance help-request indicator.
Quality	Displays the quality help-request indicator.
Tool	Displays the tool-related help-request indicator.
LED Status	Changes the indicator color when the corresponding button is clicked.
GUI	Displays the title, buttons, and LED indicators.

3. Communication Protocol
Based on the provided code, this application does not currently implement a communication protocol. It only changes LED colors locally when a button is clicked. There is no serial communication, TCP/IP, Modbus, MQTT, PLC communication, or database integration in the code.

If you plan to connect this application to an industrial controller, a simple custom serial protocol could be designed as follows:
Parameter	Proposed setting
Communication	Serial UART / RS-232 / RS-485
Baud rate	9600
Data bits	8
Parity	None
Stop bits	1
Message format	ASCII text
Production request	PROD,1
Maintenance request	MAINT,1
Quality request	QUALITY,1
Tool request	TOOL,1
Clear request	PROD,0, MAINT,0, QUALITY,0, TOOL,0

These protocol settings and message formats are proposed examples, not features already implemented in the supplied code.

4. Project Workflow
Operator clicks a department button
          
Corresponding click event executes

LED color changes

Updated status is displayed on screen


5. Software Requirements
- Python 3
- PyQt5
- QLed Python package
- Windows or Linux operating system
6. Conclusion
This project provides a simple, four-department visual Andon interface for industrial help requests. It can be extended with serial communication, PLC integration, buzzer alerts, event logging, request acknowledgment, and a central monitoring screen.

Important: The current implementation changes the LED's configured color but does not send or receive help-request messages. A real industrial deployment would need a defined communication protocol and request-state handling.
