from os import read


def convertBinToHex(bin):
    hexval = hex(int(bin, 2))[2:]
    return hexval


def convertOpcode(op):
    opcodeDict = {
        "add": "0000",
        "sll": "0000",
        "or": "0000",
        "beq": "0001",
        "sw": "0010",
        "sub": "0000",
        "nor": "0000",
        "slt": "0000",
        "bne": "0011",
        "addi": "0100",
        "j": "0101",
        "lw": "0110",
        "and": "0000",
        "nop": "0000",
        "srl": "0000",
    }
    return opcodeDict[op]


def convertFunctionBits(funcBits):
    functionDict = {
        "add": "0000",
        "sll": "0001",
        "or": "0010",
        "sub": "0011",
        "nor": "0100",
        "slt": "0101",
        "and": "0110",
        "nop": "0111",
        "srl": "1000"
    }
    return functionDict[funcBits]


def checkRegister(reg):
    registerNum = int(reg[1:])
    if registerNum > 21:
        print("Invalid register")
    return format(registerNum, "04b")


rtypeInstructions = [
    "add",
    "sll",
    "or",
    "sub",
    "nor",
    "slt",
    "and",
    "nop",
    "srl",
]

itypeInstructions = [
    "bne",
    "beq",
    "addi",
    "lw",
    "sw",
]

readf = open("inputs.txt", "r")
writef = open("outputs.raw", "w")
writef.write("v2.0 raw\n")
for _ in readf:
    splitted = _.split()

    if splitted[0] in rtypeInstructions:
        opcode = convertOpcode(splitted[0])
        funcBits = convertFunctionBits(splitted[0])
        rs = checkRegister(splitted[2])
        rt = checkRegister(splitted[3])
        rd = checkRegister(splitted[1])
        out = opcode + rs + rt + rd + funcBits
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    elif splitted[0] == "nop":
        out = "00000000000000000000"
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    elif splitted[0] in itypeInstructions:
        opcode = convertOpcode(splitted[0])
        rs = checkRegister(splitted[2])
        rt = checkRegister(splitted[1])
        im = format(int(splitted[3]), "08b")

        out = opcode + rs + rt + im
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    elif splitted[0] == "j":
        opcode = convertOpcode(splitted[0])
        target = format(int(splitted[1]), "016b")
        out = opcode + target
        print(out)
        writef.write(convertBinToHex(out) + "\n")
