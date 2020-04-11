import sys



def __write_str_as_byte(string, destination):
    byte = bytes([__string_to_bin(string)])
    destination.write(byte)


def __string_to_bin(string):
    if (len(string) == 0):
        return 0
    else:
        return (int(string[0]) * 2 ** (len(string) - 1)) + __string_to_bin(string[1:])


def complete_write(f1, f2):
    with open(f1, "r") as src:
        with open(f2, "wb") as dst:
            while True:
                # read one byte
                byte_str = src.read(8)
                byte_len = len(byte_str)

                # check if it's the end of file
                if (byte_len < 8):
                    byte_str += "1"
                    for i in range(8 - byte_len - 1):
                        byte_str += "0"
                    __write_str_as_byte(byte_str, dst)
                    break

                # write byte to the destination file
                __write_str_as_byte(byte_str, dst)


def main():
    complete_write(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
