from itertools import permutations
import sys, re

def permute_with_repeats(*args):
    return tuple(set((','.join(x) for x in permutations(args))))

if __name__ == '__main__':
    values = sys.argv[2:]
    output = sys.argv[1]
    if (not re.fullmatch('.+.txt', output)):
        print('Must enter a txt file as the first command line argument')
        exit(2)
    with open(output, 'w') as f:
        for permutation in permute_with_repeats(*values):
            f.write(permutation)
            f.write('\n')
            