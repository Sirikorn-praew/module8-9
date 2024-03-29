
# File name: TRAJECTORY.c
# Author: KRITTAPAK
# Project Name: Module8-9
# Group name: ISUS
# Modify: Dynamixel Protocal 2.0
# Send & Receive Packet
# /////   DATA FRAME  /////
# HEADER1  HEADER2  LEN   INSTRUCTION  ERROR  ADDRESS   DATA 1  ...  DATA N   Check
#  0xFF      0xFD  0-255  instruction  error  address   0-4095       0-4095    sum

from dataclasses import Field
from xml.etree.ElementTree import PI
import serial
import serial.tools.list_ports
import numpy as np
import math

# PACKET DATA
HEADER1 = 0xFF
HEADER2 = 0xFD

# INSTRUCTION
READ_DATA = 0x01
WRITE_DATA = 0x02
FACTORY_RESET = 0x03
STATUS = 0x55

# ERROR
RESULT_FAIL = 0x01
INSTRUCTION_ERROR = 0x02
SUM_ERROR = 0x03
DATA_RANGE_ERROR = 0x04
DATA_LENGTH_ERROR = 0x05
DATA_LIMIT_ERROR = 0x06
ACCESS_ERROR = 0x07

# CONTROL
NAME = 0x01
HOME_OFFSET = 0X02
MIN_POSITION_LIMIT = 0x03
MAX_POSITION_LIMIT = 0x04
MIN_SPEED_LIMIT = 0x05
MAX_SPEED_LIMIT = 0x06

# ADDRESS
HOME_CONFIGULATION = 0x10
START_STOP_MOVE = 0x11
JOINT_MOVE = 0x12
XYZ_MOVE = 0x13
GRIP_CHESS = 0x14
PRESENT_JOINT = 0x15
PRESENT_XYZ = 0x16
FIELD_CHESS = 0x17
FEEDBACK = 0x18
FIELD_ZERO = 0x19

# FIELD
PICK = 1
DROP = 2
HOME = 3
PICK2 = 4


class Uart_ISUS:
    # def __init__(self, port, baudrate, timeout):
    #     self.PORT = port
    #     self.BAUDRATE = baudrate
    #     self.DEVICE = serial.Serial()
    #     self.TIMEOUT = timeout
    #     self.iPacket = [0] * 20
    #     self.rPacket = [0] * 20
    def __init__(self):
        # self.PORT = port
        # self.BAUDRATE = baudrate
        self.DEVICE = serial.Serial()
        # self.TIMEOUT = timeout
        self.iPacket = [0] * 20
        self.rPacket = [0] * 20

        self.complete = 0
        self.presentJoint = [0] * 4
        self.presentXYZ = [0] * 4

        self.indexRPacket = 0

        # self.stack = []

    def setupUart(self):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if "CH340" in desc:
                self.DEVICE.port = port
        self.DEVICE.baudrate = 1000000
        self.DEVICE.timeout = 50
        # self.DEVICE.rs485_mode
        self.DEVICE.rts = 0
        self.DEVICE.open()

    def SHIFT_TO_LSB(self, w):
        return w & 0x00FF

    def SHIFT_TO_MSB(self, w):
        return (w >> 8) & 0x00FF

    def Sum(self, length, data):
        s = 0
        for i in range(length):
            s += data[i]
        return (~s & 0xff)

    def value_convert(self, value):
        return np.int16(value * 100)

    def Home_Configulation(self, joint_1, joint_2, joint_3, joint_4):
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = HOME_CONFIGULATION
        self.iPacket[5] = self.SHIFT_TO_LSB(np.uint(joint_1))
        self.iPacket[6] = self.SHIFT_TO_MSB(np.uint(joint_1))
        self.iPacket[7] = self.SHIFT_TO_LSB(np.uint(joint_2))
        self.iPacket[8] = self.SHIFT_TO_MSB(np.uint(joint_2))
        self.iPacket[9] = self.SHIFT_TO_LSB(np.uint(joint_3))
        self.iPacket[10] = self.SHIFT_TO_MSB(np.uint(joint_3))
        self.iPacket[11] = self.SHIFT_TO_LSB(np.uint(joint_4))
        self.iPacket[12] = self.SHIFT_TO_MSB(np.uint(joint_4))
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

    def StartStop_Move(self, joint_1, joint_2, joint_3, joint_4, gripper):
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = START_STOP_MOVE
        self.iPacket[5] = self.SHIFT_TO_LSB(np.uint(joint_1))
        self.iPacket[6] = self.SHIFT_TO_MSB(np.uint(joint_1))
        self.iPacket[7] = self.SHIFT_TO_LSB(np.uint(joint_2))
        self.iPacket[8] = self.SHIFT_TO_MSB(np.uint(joint_2))
        self.iPacket[9] = self.SHIFT_TO_LSB(np.uint(joint_3))
        self.iPacket[10] = self.SHIFT_TO_MSB(np.uint(joint_3))
        self.iPacket[11] = self.SHIFT_TO_LSB(np.uint(joint_4))
        self.iPacket[12] = np.uint(gripper)
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

    def Joint_Move(self, joint_1, joint_2, joint_3, joint_4):
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = JOINT_MOVE
        self.iPacket[5] = self.SHIFT_TO_LSB(self.value_convert(joint_1))
        self.iPacket[6] = self.SHIFT_TO_MSB(self.value_convert(joint_1))
        self.iPacket[7] = self.SHIFT_TO_LSB(self.value_convert(joint_2))
        self.iPacket[8] = self.SHIFT_TO_MSB(self.value_convert(joint_2))
        self.iPacket[9] = self.SHIFT_TO_LSB(self.value_convert(joint_3))
        self.iPacket[10] = self.SHIFT_TO_MSB(self.value_convert(joint_3))
        self.iPacket[11] = self.SHIFT_TO_LSB(self.value_convert(joint_4))
        self.iPacket[12] = self.SHIFT_TO_MSB(self.value_convert(joint_4))
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

    def XYZ_Move(self, x, y, z, roll):
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = XYZ_MOVE
        self.iPacket[5] = self.SHIFT_TO_LSB(self.value_convert(x))
        self.iPacket[6] = self.SHIFT_TO_MSB(self.value_convert(x))
        self.iPacket[7] = self.SHIFT_TO_LSB(self.value_convert(y))
        self.iPacket[8] = self.SHIFT_TO_MSB(self.value_convert(y))
        self.iPacket[9] = self.SHIFT_TO_LSB(self.value_convert(z))
        self.iPacket[10] = self.SHIFT_TO_MSB(self.value_convert(z))
        self.iPacket[11] = self.SHIFT_TO_LSB(self.value_convert(roll))
        self.iPacket[12] = self.SHIFT_TO_MSB(self.value_convert(roll))
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

    def Grip_Chess(self, value):
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = GRIP_CHESS
        self.iPacket[5] = 0x99
        self.iPacket[6] = 0x99
        self.iPacket[7] = 0x99
        self.iPacket[8] = 0x99
        self.iPacket[9] = 0x99
        self.iPacket[10] = 0x99
        self.iPacket[11] = self.SHIFT_TO_LSB(self.value_convert(value))
        self.iPacket[12] = self.SHIFT_TO_MSB(self.value_convert(value))
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

    def Field_zero(self):
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = FIELD_ZERO
        self.iPacket[5] = 0x99
        self.iPacket[6] = 0x99
        self.iPacket[7] = 0x99
        self.iPacket[8] = 0x99
        self.iPacket[9] = 0x99
        self.iPacket[10] = 0x99
        self.iPacket[11] = 0x99
        self.iPacket[12] = 0x99
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

    def radius_calculate(self, x, y):
        return math.sqrt(pow(x, 2) + pow(y, 2))

    # def Chess_grip(self, row, column, t, type):
    #     row = row.upper()
    #     list_num = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
    #     self.iPacket[0] = HEADER1
    #     self.iPacket[1] = HEADER2
    #     self.iPacket[2] = 3 + 8
    #     self.iPacket[3] = WRITE_DATA # Instruction
    #     self.iPacket[4] = FIELD_PICK
    #     self.iPacket[5] = self.SHIFT_TO_LSB(list_num[row])
    #     self.iPacket[6] = self.SHIFT_TO_MSB(list_num[row])
    #     self.iPacket[7] = self.SHIFT_TO_LSB(column)
    #     self.iPacket[8] = self.SHIFT_TO_MSB(column)
    #     self.iPacket[9] = self.SHIFT_TO_LSB(t)
    #     self.iPacket[10] = self.SHIFT_TO_MSB(t)
    #     self.iPacket[11] = self.SHIFT_TO_LSB(type)
    #     self.iPacket[12] = self.SHIFT_TO_MSB(type)
    #     self.iPacket[13] = self.Sum(13, self.iPacket)
    #     self.sendIPacket(14)

    def Chess_Pick(self, rowi, columni, rowf, columnf, name):
        self.Field_Move(rowi, columni, rowf, columnf,
                        "A", 0, "A", 0, PICK, name, 1)

    def Chess_Pick2(self, rowi, columni, rowf, columnf, rowi2, columni2, rowf2, columnf2, name, name2):
        self.Field_Move(rowi, columni, rowf, columnf, rowi2,
                        columni2, rowf2, columnf2, PICK2, name, name2)

    def Chess_Drop(self, rowi, columni, rowf, columnf, rowi2, columni2, name, name2):  # num 2 drop
        self.Field_Move(rowi, columni, rowf, columnf, rowi2,
                        columni2, "A", 0, DROP, name, name2)

    def Chess_HOME(self):
        self.Field_Move("A", 0, "A", 0, "A", 0, "A", 0, HOME, 1, 1)

    def Field_Move(self, rowi, columni, rowf, columnf, rowi2, columni2, rowf2, columnf2, type, name, name2):  # t = us
        """
                     row
             a  b  c  d  e  f  i  j
            __ __ __ __ __ __ __ __
        8  |__|__|__|__|__|__|__|__|    
        7  |__|__|__|__|__|__|__|__|
        6  |__|__|__|__|__|__|__|__|
        5  |__|__|__|__|__|__|__|__|    column
        4  |__|__|__|__|__|__|__|__|
        3  |__|__|__|__|__|__|__|__|
        2  |__|__|__|__|__|__|__|__|
        1  |__|__|__|__|__|__|__|__|


                   my robot
        """

        x = 0
        y = 0
        r = 0
        L = 400  # mm
        s = 50
        d = 0
        rowi = rowi.upper()
        rowf = rowf.upper()
        rowi2 = rowi2.upper()
        rowf2 = rowf2.upper()
        list_num = {"A": 1, "B": 2, "C": 3,
                    "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        # if list_num[row] <= 4:
        #     x = (-((5 - list_num[row])*L)/8) + (s/2)
        # elif list_num[row] >= 5:
        #     x = (((list_num[row] - 4)*L)/8) - (s/2)

        # if column <= 4:
        #     y = (-((5 - column)*L)/8) + (s/2)
        # elif column >= 5:
        #     y = (((column - 4)*L)/8) - (s/2)
        y = ((4.5 - list_num[rowi])*L)/8
        x = ((columni - 4.5)*L)/8

        r = self.radius_calculate(x, y)

        # d = math.asin(y/r)*(180/math.pi) #ref 0 degree
        # d = math.atan(y/x)*(180/math.pi)
        d = math.atan2(y, x)*(180/math.pi)
        if x >= 0 and y >= 0:
            d = d
        elif x < 0 and y >= 0:
            d = d
        elif x < 0 and y < 0:
            d = 360 + d
        elif x >= 0 and y < 0:
            d = 360 + d

        # name = name.upper()
        # list_name = {"KING":1, "QUEEN":2, "ROOK":3, "KNIGHT":3, "BISHOP":3, "PAWN":4}
        min_degree = 30
        max_degree = 55
        degree = (min_degree + (max_degree - min_degree)
                  * (name/4))  # list_name[name]/4
        degree2 = (min_degree + (max_degree - min_degree)
                   * (name2/4))  # list_name[name2]/4
        self.iPacket[0] = HEADER1
        self.iPacket[1] = HEADER2
        self.iPacket[2] = 3 + 8
        self.iPacket[3] = WRITE_DATA  # Instruction
        self.iPacket[4] = FIELD_CHESS
        self.iPacket[5] = (list_num[rowi] << 4) + columni
        self.iPacket[6] = (list_num[rowf] << 4) + columnf
        self.iPacket[7] = (list_num[rowi2] << 4) + columni2
        self.iPacket[8] = (list_num[rowf2] << 4) + columnf2
        self.iPacket[9] = self.SHIFT_TO_LSB(type)
        self.iPacket[10] = self.SHIFT_TO_MSB(type)
        self.iPacket[11] = int(degree)
        self.iPacket[12] = int(degree2)
        self.iPacket[13] = self.Sum(13, self.iPacket)
        self.sendIPacket(14)

        return [x, y, r, d]

    def sendIPacket(self, length):
        self.resetStatus()
        # initialize rPacket
        for i in range(20):
            self.rPacket[i] = 0x99
        # send Instruction Packet
        # serial
        print(self.iPacket[0:length])
        self.DEVICE.write(serial.to_bytes(self.iPacket[0:length]))

    def getRPacket(self, data):
        # print(data)
        if self.indexRPacket == 0:
            if data == HEADER1:
                # print("Header1")
                self.rPacket[self.indexRPacket] = data
                self.indexRPacket = 1
            else:
                self.indexRPacket = 0
        elif self.indexRPacket == 1:
            if data == HEADER2:
                # print("Header2")
                self.rPacket[self.indexRPacket] = data
                self.indexRPacket = 2
            else:
                self.indexRPacket = 0
        elif 2 <= self.indexRPacket <= 13:
            # print(self.indexRPacket)
            self.rPacket[self.indexRPacket] = data
            self.indexRPacket += 1
        if self.indexRPacket == 14:
            if data == self.Sum(12, self.rPacket):
                self.indexRPacket = 0
                if self.rPacket[3] == STATUS:
                    if self.rPacket[4] == FEEDBACK:
                        print("feedback")
                        self.complete = 99
                    if self.rPacket[4] == PRESENT_JOINT:
                        # print("J")
                        self.presentJoint[0] = self.rPacket[5] | (
                            (self.rPacket[6] << 8) & 0xFF00)
                        self.presentJoint[1] = self.rPacket[7] | (
                            (self.rPacket[8] << 8) & 0xFF00)
                        self.presentJoint[2] = self.rPacket[9] | (
                            (self.rPacket[10] << 8) & 0xFF00)
                        # self.presentJoint[3] = self.rPacket[11] | ((self.rPacket[12] << 8) & 0xFF00)
                        self.complete = self.rPacket[11] | (
                            (self.rPacket[12] << 8) & 0xFF00)
                    if self.rPacket[4] == PRESENT_XYZ:
                        # print("XYZ")
                        self.presentXYZ[0] = self.rPacket[5] | (
                            (self.rPacket[6] << 8) & 0xFF00)
                        self.presentXYZ[1] = self.rPacket[7] | (
                            (self.rPacket[8] << 8) & 0xFF00)
                        self.presentXYZ[2] = self.rPacket[9] | (
                            (self.rPacket[10] << 8) & 0xFF00)
                        self.presentXYZ[3] = self.rPacket[11] | (
                            (self.rPacket[12] << 8) & 0xFF00)
                return True
            else:
                self.indexRPacket = 0
        return False

    def getStatus(self):
        return self.complete

    def resetStatus(self):
        self.complete = 0

    def getPresent_Joint(self, data):
        data = data.upper()
        if data == 'J1':
            return self.presentJoint[0]
        elif data == 'J2':
            return self.presentJoint[1]
        elif data == 'J3':
            return self.presentJoint[2]
        elif data == 'J4':
            return self.presentJoint[3]

    def getPresent_XYZ(self, data):
        data = data.upper()
        if data == 'X':
            return self.presentXYZ[0]
        elif data == 'Y':
            return self.presentXYZ[1]
        elif data == 'Z':
            return self.presentXYZ[2]
        elif data == 'ROLL':
            return self.presentXYZ[3]

    def Uart_Read(self):
        # data = self.DEVICE.readall()
        # print("True")
        # if len(data) > 0:
        #     print(True)
        # print(self.DEVICE.readall())
        if self.DEVICE.readable():
            data = self.DEVICE.read(1)
            data = int.from_bytes(data, "big")
            self.getRPacket(data)
