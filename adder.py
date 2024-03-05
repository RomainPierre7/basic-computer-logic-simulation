# This file contains the implementation of an adder using the basic logic gates.

import logic_gate
import binary

class half_adder:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2
        self.and_gate = logic_gate.and_gate()
        self.xor_gate = logic_gate.xor_gate()

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_sum(self):
        self.xor_gate.set_inputs(self.input1, self.input2)
        return self.xor_gate.get_output()

    def get_carry(self):
        self.and_gate.set_inputs(self.input1, self.input2)
        return self.and_gate.get_output()
    

class full_adder:
    def __init__(self, input1=None, input2=None, carry_in=None):
        self.input1 = input1
        self.input2 = input2
        self.carry_in = carry_in
        self.half_adder1 = half_adder()
        self.half_adder2 = half_adder()
        self.or_gate = logic_gate.or_gate()

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
    

class binary_adder:
    def __init__(self, binary1=None, binary2=None):
        self.binary1 = binary1
        self.binary2 = binary2

    def set_inputs(self, binary1, binary2):
        self.binary1 = binary1
        self.binary2 = binary2

    def get_sum(self):
        self.binary1, self.binary2 = binary.give_same_length(self.binary1, self.binary2)
        carry = 0
        result = ''
        for i in range(len(self.binary1)-1, -1, -1):
            fa = full_adder(self.binary1[i], self.binary2[i], carry)
            carry = fa.get_carry()
            result = str(fa.get_sum()) + result
        if carry:
            return str(carry) + result
        return result