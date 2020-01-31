import sys

def read_num(string):
    items = []
    for idx, char in enumerate(string):
        if not char.isdigit():
            return (string[0:idx], string[idx:])

def read_cmd(string):
    addr, rest = read_num(string)
    maxlen, rest = read_num(rest[1:])
    replace = rest[1:]
    return (int(addr), int(maxlen), replace)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        in_file = sys.argv[1]
        strings_file = sys.argv[2]

        with open(strings_file, 'r') as sf:
            lines = sf.read().splitlines()

        encoding = lines[0]

        items = []
        for line in lines:
            if len(line) > 0 and line[0] == '@':
                addr, maxlen, replace = read_cmd(line[1:])
                replace = replace.encode(encoding)
                if len(replace) > maxlen:
                    raise Exception('Replacement for ' + str(addr) + ' is ' + str(len(replace)) + ' bytes long (> ' + str(maxlen) + ')!')
                items.append((addr, maxlen, replace))

        with open(in_file, 'rb+') as outf:
            for addr, maxlen, replace in items:
                outf.seek(addr)
                outf.write(replace)
                outf.write(bytearray([0] * (maxlen - len(replace))))

    else:
        print('Usage: python string-replace.py FILE STRINGS_FILE')
