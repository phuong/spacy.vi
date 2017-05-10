DEFAULT_DELIMITER = '\n'.encode('utf-8')


def from_file(path, delimiter=DEFAULT_DELIMITER):
    file = open(path, 'r')
    data = file.read()
    file.close()
    if delimiter:
        return data.rstrip().split(delimiter)
    return data
