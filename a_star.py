# Copyright Pololu Corporation.  For more information, see https://www.pololu.com/
import smbus #System Management Bus. Je modul za I2C komunikacijo med RPI in Arduino
import struct #Je tisti modul, ki skrbi za pakiranje, posiljanje in sprejemanje podatkov od RPi do Arduina.
import time


class AStar(object):
  def __init__(self):
    self.bus = smbus.SMBus(1)






  def read_unpack(self, address, size, format):
        # A delay of 0.0001 (100 us) after each write is enough to account
    # for the worst-case situation in our example code.

    self.bus.write_byte(20,address)
    time.sleep(0.0001)
    byte_list = []
    for n in range(0,size):
      byte_list.append(self.bus.read_byte(20))
    return struct.unpack(format,bytes(bytearray(byte_list)))

  def write_pack(self, address, format, *data):
    data_array = map(ord, list(struct.pack(format, *data)))
self.bus.write_i2c_block_data(20, address, data_array)
    time.sleep(0.0001)





  def leds(self, red, yellow, green):
    self.write_pack(0, 'BBB', red, yellow, green)

  def play_notes(self, notes):
    self.write_pack(26, 'B15s', 1, notes.encode("ascii"))

  def motors(self, left, right):
    self.write_pack(8, 'hh', left, right)

  def read_buttons(self):
    return self.read_unpack(3, 3, "???")

  def read_battery_millivolts(self):
    return self.read_unpack(12, 2, "H")

  def read_analog(self):
    return self.read_unpack(14, 12, "HHHHHH")

  def servo_motor(self, left, right):
    return self.write_pack(6, 'BB', left, right)

  def test_read8(self):
    self.read_unpack(0, 8, 'cccccccc')

  def test_write8(self):
    self.bus.write_i2c_block_data(20, 0, [0,0,0,0,0,0,0,0])
    time.sleep(0.0001)
