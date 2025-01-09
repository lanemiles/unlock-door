import serial

# Replace 'COM3' with your Arduino's serial port (e.g., 'COMx' on Windows or '/dev/ttyUSBx' on Linux/Mac)
arduino_port = "/dev/tty.usbmodem101"
baud_rate = 9600

# Establish a connection to the Arduino
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)

def send_command(command):
    """
    Sends a command ('ON' or 'OFF') to the Arduino and prints the response.
    """
    command = command.strip() + '\n'  # Add newline character for Arduino
    arduino.write(command.encode())  # Send command to Arduino
    response = arduino.readline().decode().strip()  # Read response
    print(f"Arduino: {response}")

def main():
    print("Type 'ON' to turn the relay on, 'OFF' to turn it off, or 'EXIT' to quit.")
    while True:
        user_input = input("Enter command: ").strip().upper()
        if user_input == "EXIT":
            print("Exiting...")
            break
        elif user_input in ["ON", "OFF"]:
            send_command(user_input)
        else:
            print("Invalid command. Please type 'ON', 'OFF', or 'EXIT'.")

    arduino.close()  # Close the serial connection

if __name__ == "__main__":
    main()