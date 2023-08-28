# main.py -- put your code here!
import machine
import time
import sys
import ucsv
from machine import I2C, Pin

i2c = I2C(scl=Pin(22), sda=Pin(21))

AT24C2 = 0x50


if not AT24C2 in i2c.scan():
    print("Could not find AT24C2")
    sys.exit()

def write_data_to_AT24C2(data):
    address = 0x00  # Starting address in AT24C256
    data_bytes = bytearray([address >> 8, address & 0xFF]) + bytearray(data)
    i2c.writeto(AT24C2, data_bytes)

if __name__ == "__main__":
    # Example data to be saved
    df = [23,12,22,24,30]
    data_to_save = df

    write_data_to_AT24C2(data_to_save)
    print("Data saved successfully!")

if not AT24C2 in i2c.scan():
    print("Could not find AT24C256")
    sys.exit()

def read_AT24C2_data(address, length):
    address_bytes = bytearray([address >> 8, address & 0xFF])
    i2c.writeto(AT24C2, address_bytes)
    time.sleep_ms(5)  # Delay to allow the EEPROM to process the address
    result = bytearray(length)
    i2c.readfrom_into(AT24C2, result)
    return result

if __name__ == "__main__":
    data = read_AT24C2_data(0x0000, 10)  # Read 10 bytes starting from address 0x0000
    print("Data read from AT24C2:", [int(byte) for byte in data])



