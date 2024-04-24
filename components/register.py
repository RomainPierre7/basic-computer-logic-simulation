class Register:
    def __init__(self, bit_length):
        self.bit_length = bit_length
        self.register = "0" * bit_length

    def read_register(self):
        return self.register

    def write_register(self, value):
        if isinstance(value, str) and len(value) == self.bit_length and all(bit in '01' for bit in value):
            self.register = value
        else:
            print(f"Invalid input. Please provide an {self.bit_length}-bit binary string.")

    def clear_register(self):
        self.register = "0" * self.bit_length

    def get_value(self):
        return int(self.register, 2)
    
    def set_value(self, value):
        self.register = format(value, f'0{self.bit_length}b')