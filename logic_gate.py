# Description: This file contains the classes for the basic logic gates.

# Inputs could be 0 or 1 (as integers), but also '0' or '1' (as strings) for easier input validation.

# -------------------- Main Gates --------------------

class NotGate:
    def __init__(self, input=0):
        self.input = int(input)

    def set_input(self, input):
        self.input = int(input)

    def get_output(self):
        return 1 - self.input


class AndGate:
    def __init__(self, input1=0, input2=0):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        return self.input1 * self.input2

class OrGate:
    def __init__(self, input1=0, input2=0):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        return max(self.input1, self.input2)

# -------------------- Derived Gates --------------------

class NandGate:
    def __init__(self, input1=0, input2=0):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        return NotGate(AndGate(self.input1, self.input2).get_output()).get_output()


class NorGate:
    def __init__(self, input1=0, input2=0):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        return NotGate(OrGate(self.input1, self.input2).get_output()).get_output()


class XorGate:
    def __init__(self, input1=0, input2=0):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        input1_and_not_input2 = AndGate(self.input1, NotGate(self.input2).get_output()).get_output()
        not_input1_and_input2 = AndGate(NotGate(self.input1).get_output(), self.input2).get_output()
        return OrGate(input1_and_not_input2, not_input1_and_input2).get_output()


class XnorGate:
    def __init__(self, input1=0, input2=0):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def set_inputs(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)

    def get_output(self):
        input1_and_not_input2 = AndGate(self.input1, NotGate(self.input2).get_output()).get_output()
        not_input1_and_input2 = AndGate(NotGate(self.input1).get_output(), self.input2).get_output()
        return NotGate(OrGate(input1_and_not_input2, not_input1_and_input2).get_output()).get_output()

# -------------------- Functions --------------------
    
def print_truth_table(gate):
    gate_name = gate.__class__.__name__[:-4].upper()
    print("Truth Table for " + gate_name + " gate:\n")
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