# Description: This file contains the classes for the basic logic gates.

# Inputs could be 0 or 1 (as integers), but also '0' or '1' (as strings) for easier input validation.

# -------------------- Main Gates --------------------

class NotGate:
    def __init__(self):
        self.input = 0

    def set_input(self, input):
        self.input = int(input)

    def get_output(self):
        return 1 - self.input


class AndGate:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        return self.input1 * self.input2

class OrGate:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        return max(self.input1, self.input2)

# -------------------- Derived Gates --------------------

class NandGate:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        self.and_gate.set_inputs(self.input1, self.input2)
        self.not_gate.set_input(self.and_gate.get_output())
        return self.not_gate.get_output()


class NorGate:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        self.or_gate.set_inputs(self.input1, self.input2)
        self.not_gate.set_input(self.or_gate.get_output())
        return self.not_gate.get_output()


class XorGate:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.and_gate1 = AndGate()
        self.and_gate2 = AndGate()
        self.not_gate1 = NotGate()
        self.not_gate2 = NotGate() 
        self.or_gate = OrGate() 

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        self.not_gate1.set_input(self.input1)
        self.not_gate2.set_input(self.input2)
        self.and_gate1.set_inputs(self.input1, self.not_gate2.get_output())
        self.and_gate2.set_inputs(self.not_gate1.get_output(), self.input2)
        self.or_gate.set_inputs(self.and_gate1.get_output(), self.and_gate2.get_output())
        return self.or_gate.get_output()


class XnorGate:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.and_gate1 = AndGate()
        self.and_gate2 = AndGate()
        self.not_gate1 = NotGate()
        self.not_gate2 = NotGate()
        self.not_gate3 = NotGate()
        self.or_gate = OrGate() 

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        self.not_gate1.set_input(self.input1)
        self.not_gate2.set_input(self.input2)
        self.and_gate1.set_inputs(self.input1, self.not_gate2.get_output())
        self.and_gate2.set_inputs(self.not_gate1.get_output(), self.input2)
        self.or_gate.set_inputs(self.and_gate1.get_output(), self.and_gate2.get_output())
        self.not_gate3.set_input(self.or_gate.get_output())
        return self.not_gate3.get_output()

# -------------------- Functions --------------------
    
def print_truth_table(gate):
    gate_name = gate.__class__.__name__[:-4].upper()
    print("Truth table for " + gate_name + " gate:\n")
    if gate_name == "NOT":
        print("Input | Output")
        print("------|-------")
        for i in range(2):
            gate.set_input(i)
            print("  " + str(i) + "   |   " + str(gate.get_output()))
    else:
        print("Input 1 | Input 2 | Output")
        print("--------|---------|-------")
        for i in range(2):
            for j in range(2):
                gate.set_inputs(i, j)
                print("   " + str(i) + "    |    " + str(j) + "    |   " + str(gate.get_output()))
    print("\n\n")

def print_all_truth_tables():
    print_truth_table(NotGate())
    print_truth_table(AndGate())
    print_truth_table(OrGate())
    print_truth_table(NandGate())
    print_truth_table(NorGate())
    print_truth_table(XorGate())
    print_truth_table(XnorGate())