def read_rows(lines : list[str]) -> list[dict]:
    l = []
    header = None
    for line in lines:
        if not line.strip():
            continue
        if header is None:
                header = line.strip().split(',')
                continue
        values = line.strip().split(',')
        if len(values) != len(header):
            continue
        row = {}
        for i in range(len(header)):
            row[header[i].strip()] = values[i].strip()
        l.append(row)
    return l
