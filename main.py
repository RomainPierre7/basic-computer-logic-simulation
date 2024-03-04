import logic_gate
import adder

def main():
    fa = adder.full_adder()
    fa.set_inputs(1, 1, 1)
    print(fa.get_carry())

if __name__ == "__main__":
    main()