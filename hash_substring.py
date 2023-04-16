def read_input():
    input_type = input().strip().upper()

    if input_type == "I":
        pattern = input().strip()
        text = input().strip()
        return (input_type, pattern, text)
    elif input_type == "F":
        with open("tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
        return (input_type, pattern, text)
    else:
        exit()


def rabin_karp(pattern, text):
    p = len(pattern)
    t = len(text)
    if p > t:
        return []

    prime = 1000000007
    multiplier = 263
    pattern_hash = 0
    text_hash = 0
    result = []
    h = 1

    for i in range(p - 1):
        h = (h * multiplier) % prime

    for i in range(p):
        pattern_hash = (pattern_hash * multiplier + ord(pattern[i])) % prime
        text_hash = (text_hash * multiplier + ord(text[i])) % prime

    for i in range(t - p + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + p]:
                result.append(i)
        if i < t - p:
            text_hash = (multiplier * (text_hash - ord(text[i]) * h) + ord(text[i + p])) % prime
            if text_hash < 0:
                text_hash += prime
    return result


def print_occurrences(occurrences):
    print(" ".join(str(x) for x in occurrences))


if __name__ == '__main__':
    input_type, pattern, text = read_input()
    occurrences = rabin_karp(pattern, text)
    print_occurrences(occurrences)


def print_occurrences(occurrences):

    if occurrences:
        print(end="")
        print(*occurrences)
    else:
        print("error")


if __name__ == '__main__':
    input_type = get_input_type()
    if input_type == 'K':
        pattern, text = read_from_keyboard()
    else:
        pattern, text = read_from_file()
    occurrences = find_occurrences(pattern, text)
    print_occurrences(occurrences)
