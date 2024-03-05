import logic_gate
import adder
import register

import random

def main():
    ARCHITECURE = 8 # 8-bit architecture (can be changed to any value (e.g. 4, 16, 32, 64, 128, 256, etc.))

    print(f"Example of adding two {ARCHITECURE}-bit numbers (unsigned int range: 0 to {2 ** ARCHITECURE - 1})")

    reg1 = register.Register(ARCHITECURE)
    reg2 = register.Register(ARCHITECURE)
    reg1.set_value(random.randint(0, 2 ** ARCHITECURE - 1))
    reg2.set_value(random.randint(0, 2 ** ARCHITECURE - 1))

    adder1 = adder.RegisterAdder(ARCHITECURE)
    adder1.set_registers(reg1.read_register(), reg2.read_register())

    reg3 = register.Register(ARCHITECURE)
    reg3.write_register(adder1.get_sum())

    print(f"R1: {reg1.read_register()} ({reg1.get_value()})")
    print(f"R2: {reg2.read_register()} ({reg2.get_value()})")
    print(f"R3: {reg3.read_register()} ({reg3.get_value()})")

if __name__ == "__main__":
    main()