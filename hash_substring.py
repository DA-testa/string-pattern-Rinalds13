# python3

def read_input():
    ievade = input()
    if ievade.startswith('F'):
        with open('tests/06', 'r') as f:
            modelis, teksts = map(str.strip, f.readlines())
    else:
        modelis, teksts = input().strip(), input().strip()
    return teksts, modelis
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    indeks = []
    pg, tg = len(pattern), len(text)
    ag, q = 256, 1

    for i in range(pg - 1):
        q = (q * ag)
    hash_ver = nev = i = j = h = 0
    # and return an iterable variable
    return [0]
    
    for i in range(pg):
    hash_ver = (hash_ver * ag + ord(pattern[i])) % q
    nev = (nev * ag + ord(text[i])) % q
    if i < pg - 1:
        h = (ag * h + 1) % q


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

