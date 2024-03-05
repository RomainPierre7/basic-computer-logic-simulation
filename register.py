class EightBitRegister:
    def __init__(self):
        self.register = "00000000"

    def read_register(self):
        return self.register

    def write_register(self, value):
        if isinstance(value, str) and len(value) == 8 and all(bit in '01' for bit in value):
            self.register = value
        else:
            print("Invalid input. Please provide an 8-bit binary string.")

    def clear_register(self):
        self.register = "00000000"

    def get_value(self):
        return int(self.register, 2)
    
    def set_value(self, value):
        self.register = format(value, '08b')