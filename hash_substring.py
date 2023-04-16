def read_input():
    c = input()
    if c.startswith('F'):
        with open('tests/06', 'r') as f:
            pattern, text = map(str.strip, f.readlines())
    else:
        pattern, text = input().strip(), input().strip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    ind = []
    p_len, t_len = len(pattern), len(text)
    a_len, q = 256, 1
    for i in range(p_len - 1):
        q = (a_len * q)
    phash_val = thash_val = i = j = h = 0
    for i in range(p_len):
        phash_val = (a_len * phash_val + ord(pattern[i])) % q
        thash_val = (a_len * thash_val + ord(text[i])) % q
        if i < p_len - 1:
            h = (a_len * h + 1) % q
    for i in range(t_len - p_len + 1):
        if phash_val == thash_val and pattern == text[i:i+p_len]:
            ind.append(str(i))
        if i < t_len - p_len:
            thash_val = (a_len * (thash_val - ord(text[i]) * h) + ord(text[i + p_len])) % q
    return ind

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
