import logic_gate
import adder
import register

import random

def main():
    #logic_gate.print_all_truth_tables()
    print("Example of adding two 8-bit numbers:")

    reg1 = register.EightBitRegister()
    reg2 = register.EightBitRegister()
    reg1.set_value(random.randint(0, 255))    
    reg2.set_value(random.randint(0, 255))


    adder1 = adder.EightBitAdder()
    adder1.set_registers(reg1.read_register(), reg2.read_register())

    reg3 = register.EightBitRegister()
    reg3.write_register(adder1.get_sum())

    print(f"R1: {reg1.read_register()} ({reg1.get_value()})")
    print(f"R2: {reg2.read_register()} ({reg2.get_value()})")
    print(f"R3: {reg3.read_register()} ({reg3.get_value()})")

if __name__ == "__main__":
    main()