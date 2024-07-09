from itertools import permutations
import sys

def permute_with_repeats(*args):
    return set((','.join(x) for x in permutations(args)))

if __name__ == '__main__':
    values = sys.argv[2:]
    output = sys.argv[1]
    with open(output, 'w') as f:
        for permutation in permute_with_repeats(*values):
            f.write(permutation)
            f.write('\n')
            