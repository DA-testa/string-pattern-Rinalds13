def get_input_type():
    while True:
        input_type = input().strip().upper()
        if input_type in ('K', 'F'):
            return input_type
        else:
            print("error")


def read_from_keyboard():
    pattern = input().strip()
    text = input().strip()
    return pattern, text


def read_from_file():
    filename = input()
    with open(filename) as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
    return pattern, text


def find_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    pattern_hash = sum(ord(pattern[i]) * pow(10, p - i - 1) for i in range(p))
    text_hash = sum(ord(text[i]) * pow(10, p - i - 1) for i in range(p))
    occurrences = []
    for i in range(t - p + 1):
        if pattern_hash == text_hash and pattern == text[i:i+p]:
            occurrences.append(i)
        if i < t - p:
            text_hash = (text_hash - ord(text[i]) * pow(10, p - 1)) * 10 + ord(text[i+p])
    return occurrences


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
