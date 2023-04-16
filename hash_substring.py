# python3
# Rinalds Ulmanis, 7.grupa 221RDB152


def read_input():
    ievade = input()

    if "F" in ievade:
        Fails = 'tests/06'
        with open(Fails, 'r') as f:
            pattern = f.readline().rstrip()
            teksts = f.readline().rstrip()

    elif "I" in ievade:
        pattern = input().rstrip()
        teksts = input().rstrip()

    return pattern, teksts


def print_occurrences(output):
    print(' '.join(str(x) for x in output))


def get_occurrences(pattern, text):
    ag = 256
    pg = len(pattern)
    tg = len(text)
    q = 101

    indeks = []
    p_hash = 0
    t_hash = 0
    h = 1

    for i in range(pg - 1):
        h = (h * ag) % q

    for i in range(pg):
        p_hash = (ag * p_hash + ord(pattern[i])) % q
        t_hash = (ag * t_hash + ord(text[i])) % q

    for i in range(tg - pg + 1):
        if p_hash == t_hash:
            if pattern == text[i:i + pg]:
                indeks.append(i)

        if i < tg - pg:
            t_hash = (ag * (t_hash - ord(text[i]) * h) + ord(text[i + pg])) % q
            t_hash = (t_hash + q) % q

    return indeks


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
