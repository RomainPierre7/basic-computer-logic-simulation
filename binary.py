# Description: This file contains some utility functions for binary operations.

def get_binary_value(base_10_value):
    return bin(base_10_value)[2:]

def get_base_10_value(binary_value):
    return int(binary_value, 2)
    
def give_same_length(binary1, binary2):
    if len(binary1) > len(binary2):
        binary2 = '0' * (len(binary1) - len(binary2)) + binary2
    elif len(binary2) > len(binary1):
        binary1 = '0' * (len(binary2) - len(binary1)) + binary1
    return binary1, binary2