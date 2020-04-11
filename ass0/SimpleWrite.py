import sys



def __write_str_as_byte(string, destination):
    byte = bytes([__string_to_bin(string)])
    destination.write(byte)


def __string_to_bin(string):
    if (len(string) == 0):
        return 0
    else:
        return (int(string[0]) * 2 ** (len(string) - 1)) + __string_to_bin(string[1:])


def __get_block_generator(source):
    while True:
        block = source.read(8)
        if (block == ""):
            break
        yield block
    yield -1


# translates character sequence (which only consists of zeros and ones)
# of f1 into bits and writes them in f2
def simple_write(f1, f2):
    with open(f1, "r") as src:
        with open(f2, "wb") as dst:
            gen = __get_block_generator(src)
            while True:
                block = next(gen)
                if (block == -1):
                    break
                __write_str_as_byte(str(block), dst)

def main():
    simple_write(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
