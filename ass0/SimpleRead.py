import sys



# this generator yields next bit (0 or 1) if present, yields -1 otherwise
def __get_bit_generator(source):
    while True:
        # read first byte since python can't read bits
        byte = source.read(1)
        if (byte == b""):
            break
        for i in range(0, 8):
            # convert byte to int (for performing bitwise operations)
            # shift i bits to the right and check if first bit is 1
            firstbit = (ord(byte) << i) & 128
            if (firstbit == 0):
                yield 0
            else:
                yield 1
    yield -1


# writes '1' or '0' in destination file, depending on the first argument
def __write_bit_as_str(bit, destination):
    destination.write(str(bit))


# writes bits from first file to second file as the char sequence of zeros and ones 
def simple_read(f1, f2):
    # open both files
    with open(f1, "rb") as src:
        with open(f2, "w") as dst:
            gen = __get_bit_generator(src)
            while True:
                bit = next(gen)
                if (bit == -1):
                    break
                __write_bit_as_str(bit, dst)


def main():
    # it's assumed that argument count is two
    simple_read(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
