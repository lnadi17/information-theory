import sys


def __bin_to_string(binary):
    # convert bytes object to int first
    integer = ord(binary)
    result = "XXXXXXXX"

    # construct corresponding string
    for i in range(8):
        rem = integer % 2
        integer = integer // 2
        result = result.replace("X", str(rem), 1)

    # reverse result and return
    return result[::-1]
    

def __write_byte_as_string(byte, destination):
    destination.write(__bin_to_string(byte))
    print(__bin_to_string(byte))


def complete_read(f1, f2):
    with open(f1, "rb") as src:
        with open(f2, "w") as dst:
            # read 2 bytes at a time
            current_b = src.read(1)
            next_b = src.read(1)

            while True:
                # if next byte is empty, remove unnecessary bits, write them in dst and break
                if (len(next_b) == 0):
                    byte_str = __bin_to_string(current_b)
                    # save the index from which the tail starts
                    last_unneeded_index = -1
                    for i in reversed(range(len(byte_str))):
                        if (byte_str[i] == "1"):
                            last_unneeded_index = i
                            break
                    byte_str = byte_str[:last_unneeded_index]
                    dst.write(byte_str)
                    break

                __write_byte_as_string(current_b, dst)
                current_b = next_b
                next_b = src.read(1)


def main():
    complete_read(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
