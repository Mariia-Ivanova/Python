d = {}

with open('al.txt') as f:
    for line in f:
        items = line.split('-')
        eng = items[0].strip()
        lat = items[1].split(',')
        for lat_word in lat:
            lat_word = lat_word.strip()
            if lat_word in d:
                d[lat_word].append(eng)
            else:
                d[lat_word] = [eng]
d = dict(sorted(d.items()))
for key, value in d.items():
    print(f'{key} - {", ".join(value)}')

