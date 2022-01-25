# test copy.py

from complicatedWiresModule import complicatedWires

def main():
    foo = complicatedWires(parallel=True, snEven=True)

    foo.addWire(True, True, False, True)

    print(foo.wires[0].isRed)

    print(foo.returnInstructions())




if __name__ == "__main__":
    main()

