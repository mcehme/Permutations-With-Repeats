# Permutations-With-Repeats
A simple project for a math Prof. who needed all permutations of a list with repeating elements. Duplicate permutations are removed.

## Option 1: EXE
Download and use the EXE (on Windows platforms).

EXE is found in ./dist

Note: Run installer script on target platform to create executable for non-Windows platforms.

## Option 2: Command line
Run the program as a command line utility. 


```
py permute.py output_filename.txt 1 2 3 4 5
```

output_filename.txt is the filename to output the results. It must be a txt file.

Any number of inputs is acceptable; however, they must be separated by spaces.

## Option 3: Import function
Place the file in the same directory as your current script.

```python
import permute


permute.permute_with_repeats('arg1', 'arg2', 'arg3')
#OR
args = ['arg1', 'arg2', 'arg3']
permute.permute_with_repeats(*args)

```

## Option 4: Copy and Paste

Copy and paste the below function into your script.

```python
def permute_with_repeats(*args):
    from itertools import permutations
    return tuple(set((','.join(x) for x in permutations(args))))
```