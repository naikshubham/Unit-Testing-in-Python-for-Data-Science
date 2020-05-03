def row_to_list(row):
    # "2,081\t314,942\n"
    try:
        f = row.split('\t')[0]
        s = row.split('\t')[1].split(',')[0]
        t = row.split('\t')[1].split(',')[1].split('\n')[0]
        result = [f, s, t]
    except IndexError:
        result = None
    return result

def convert_to_int(value):
    value = value.replace(',', '')
    return int(value)