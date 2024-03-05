import logic_gate
import adder
import binary

import random

def main():
    print("Example of adding two binary numbers:")

    binary1 = binary.get_binary_value(random.randint(0, 30))
    binary2 = binary.get_binary_value(random.randint(0, 30))
    bin_adder = adder.binary_adder(binary1, binary2)

    sum = bin_adder.get_sum()

    print(f"Binary 1: {binary1} ({binary.get_base_10_value(binary1)})")
    print(f"Binary 2: {binary2} ({binary.get_base_10_value(binary2)})")
    print(f"Sum: {sum} ({binary.get_base_10_value(sum)})")

if __name__ == "__main__":
    main()