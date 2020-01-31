import sys

if __name__ == '__main__':
    if len(sys.argv) == 5:
        filename = sys.argv[1]
        start = int(sys.argv[2], 0)
        end = int(sys.argv[3], 0)
        encoding = sys.argv[4]
        with open(filename, 'rb') as f:
            f.seek(start)
            data = f.read(end - start)

        items = []

        curr_item = []
        curr_start = 0
        in_string = True
        for offset, byte in enumerate(data):
            if in_string:
                if byte != 0:
                    curr_item.append(byte)
                else:
                    in_string = False
            else:
                if byte == 0:
                    continue
                else:
                    try:
                        string = bytearray(curr_item).decode(encoding)
                        items.append((string, start + curr_start, offset - curr_start - 1))
                    except:
                        pass
                    curr_item = [byte]
                    curr_start = offset
                    in_string = True

        print('Found ' + str(len(items)) + ' strings')
        with open('strings.txt', 'w') as outf:
            outf.write(encoding + '\n\n')
            for string, offset, maxlen in items:
                outf.write('# "' + string + '"\n')
                outf.write('#@' + str(offset) + '-' + str(maxlen) + '=\n\n')

    else:
        print('Usage: python string-finder.py FILE START END ENCODING')
