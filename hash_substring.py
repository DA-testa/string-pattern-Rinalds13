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
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

