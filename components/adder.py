# This file contains the implementation of an adder using the basic logic gates.

from components import logic_gate
from components import register

class HalfAdder:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.and_gate = logic_gate.AndGate()
        self.xor_gate = logic_gate.XorGate()

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_sum(self):
        self.xor_gate.set_inputs(self.input1, self.input2)
        return self.xor_gate.get_output()

    def get_carry(self):
        self.and_gate.set_inputs(self.input1, self.input2)
        return self.and_gate.get_output()
    

class FullAdder:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.carry_in = 0
        self.half_adder1 = HalfAdder()
        self.half_adder2 = HalfAdder()
        self.or_gate = logic_gate.OrGate()

    def set_inputs(self, input1, input2, carry_in):
        self.input1 = input1
        self.input2 = input2
        self.carry_in = carry_in

    def get_sum(self):
        self.half_adder1.set_inputs(self.input1, self.input2)
        self.half_adder2.set_inputs(self.half_adder1.get_sum(), self.carry_in)
        return self.half_adder2.get_sum()

    def get_carry(self):
        self.half_adder1.set_inputs(self.input1, self.input2)
        self.half_adder2.set_inputs(self.half_adder1.get_sum(), self.carry_in)
        self.or_gate.set_inputs(self.half_adder1.get_carry(), self.half_adder2.get_carry())
        return self.or_gate.get_output()
    

class RegisterAdder:
    def __init__(self, bit_length):
        self.bit_length = bit_length
        self.register1 = register.Register(bit_length)
        self.register2 = register.Register(bit_length)
        self.full_adders = [FullAdder() for _ in range(bit_length)]
    
    def set_registers(self, register1, register2):
        self.register1.write_register(register1)
        self.register2.write_register(register2)

    def get_sum(self):
        sum = ""
        carry = 0
        for i in range(self.bit_length-1, -1, -1):
            self.full_adders[i].set_inputs(int(self.register1.read_register()[i]), int(self.register2.read_register()[i]), carry)
            sum = str(self.full_adders[i].get_sum()) + sum
            carry = self.full_adders[i].get_carry()
        return sum