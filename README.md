# basic-computer-logic-simulation

This is a simple computer logic simulation. It includes the basic components of a computer architecture, such as logic gates, adders, registers, and more.

All the components are implemented using Python classes and generalized to any bit size architecture.

## How to run
```bash
python3 main.py
```

> **Note**: The `main` file simply presents some examples of the implemented components. Feel free to modify it as a **playground**.

## Vulgarization

The main components of a computer architecture are:
- Processor (CPU)
- Memory
- Input/Output (I/O)

This project focuses on the **Processor** part, which is the brain of the computer. It is composed of several components, such as:
- Registers
- Arithmetic Logic Unit (ALU)
- Control Unit (CU) => *Not implemented in this project*

The **Registers** are the memory units of the processor. They are used to store data temporarily during the execution of a program. In this project, the value of a register is represented by a string of bits (e.g., "10101010" for an 8-bit register).

The **Arithmetic Logic Unit (ALU)** is the part of the processor that performs arithmetic and logical operations. It is composed of several components, such as:
- Logic gates
- Adders
- Multiplexers
- Demultiplexers
- Shifters
- Comparators
- ...

# Components

- [Logic gates](#logic-gates)
- [Adder](#adder)
- [Arithmetic Logic Unit (ALU)](#arithmetic-logic-unit-alu)
- [Processor Registers](#processor-registers)
- [Processor (CPU)](#processor-cpu)
- [Memory](#memory)

## Logic gates

### Main gates
- NOT
- AND
- OR

### Derived gates
- NAND
- NOR
- XOR
- XNOR

**Wikipedia**: https://en.wikipedia.org/wiki/Logic_gate

## Adder

- Half Adder
- Full Adder
- n-bit Adder

**Wikipedia**: https://en.wikipedia.org/wiki/Adder_(electronics)

## Arithmetic Logic Unit (ALU)

- TODO

**Wikipedia**: https://en.wikipedia.org/wiki/Arithmetic_logic_unit

## Processor Registers

- n-bit Register

**Wikipedia**: https://en.wikipedia.org/wiki/Processor_register

## Processor (CPU)

- TODO

### Instruction set

- TODO

**Wikipedia**: https://en.wikipedia.org/wiki/Central_processing_unit

## Memory

- TODO

**Wikipedia**: https://en.wikipedia.org/wiki/Computer_memory