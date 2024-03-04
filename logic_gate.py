# Description: This file contains the classes for the basic logic gates.

# -------------------- Main Gates --------------------

class not_gate:
    def __init__(self, input=None):
        self.input = input

    def set_input(self, input):
        self.input = input

    def get_output(self):
        return 1 - self.input


class and_gate:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        return self.input1 * self.input2

class or_gate:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        return max(self.input1, self.input2)

# -------------------- Derived Gates --------------------

class nand_gate:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        return not_gate(and_gate(self.input1, self.input2).get_output()).get_output()


class nor_gate:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        return not_gate(or_gate(self.input1, self.input2).get_output()).get_output()


class xor_gate:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        input1_and_not_input2 = and_gate(self.input1, not_gate(self.input2).get_output()).get_output()
        not_input1_and_input2 = and_gate(not_gate(self.input1).get_output(), self.input2).get_output()
        return or_gate(input1_and_not_input2, not_input1_and_input2).get_output()


class xnor_gate:
    def __init__(self, input1=None, input2=None):
        self.input1 = input1
        self.input2 = input2

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        input1_and_not_input2 = and_gate(self.input1, not_gate(self.input2).get_output()).get_output()
        not_input1_and_input2 = and_gate(not_gate(self.input1).get_output(), self.input2).get_output()
        return not_gate(or_gate(input1_and_not_input2, not_input1_and_input2).get_output()).get_output()

# -------------------- Functions --------------------
    
def print_truth_table(gate):
    print("Truth Table for " + gate.__class__.__name__.split('_')[0].upper() + " gate:\n")
    if len(vars(gate)) == 1:
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
    print_truth_table(not_gate())
    print_truth_table(and_gate())
    print_truth_table(or_gate())
    print_truth_table(nand_gate())
    print_truth_table(nor_gate())
    print_truth_table(xor_gate())
    print_truth_table(xnor_gate())