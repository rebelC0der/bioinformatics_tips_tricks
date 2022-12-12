from re import findall
from time import perf_counter


# Generic, for loop solution:
def count_kmer_loop(sequence, kmer):
    kmer_count = 0
    for position in range(len(sequence) - (len(kmer) - 1)):
        if sequence[position:position + len(kmer)] == kmer:
            kmer_count += 1
    return kmer_count


"""
if sequence[position:position + len(kmer)] == kmer
...
if AAT[TAA]AAC == AAA | do nothng
if AATT[AAA]AC == AAA | add 1 to count
...
"""


# List comprehension solution:
def count_kmer_listcomp(sequence, kmer):
    kmer_list = [sequence[pos:pos + len(kmer)]
                 for pos in range(len(sequence) - (len(kmer) - 1))]
    return kmer_list.count(kmer)


"""
seq = "AATTAAAAC"
kmer = "AAA"
kmer_list <= add [AAT]TAAAAC
kmer_list <= add A[ATT]AAAAC
kmer_list <= add AA[TTA]AAAC
...
count "AAA" in kmer_list
"""


# RegExp solution:
def count_kmer_regexp(sequence, kmer):
    return len(findall(f'(?=({kmer}))', seq))


# Test Area
seq = "AAATTAAAAAC" * 1000000
kmer = "AA"

# ==
start_time = perf_counter()

print("Loop k-mer count: ", end='')
print(count_kmer_loop(seq, kmer))

elapsed_time = perf_counter()
print(f'Loop took: {(elapsed_time - start_time):0.6f}s\n')
# ==

# ==
start_time = perf_counter()

print("List comprehension k-mer count: ", end='')
print(count_kmer_listcomp(seq, kmer))

elapsed_time = perf_counter()
print(f'List comprehension took: {(elapsed_time - start_time):0.6f}s\n')
# ==

# ==
start_time = perf_counter()

print("RegExp k-mer count: ", end='')
print(count_kmer_regexp(seq, kmer))

elapsed_time = perf_counter()
print(f'RegExp took: {(elapsed_time - start_time):0.6f}s\n')
# ==

"""
Useful links about regular expressions in Python:
1. Regular Expressions generator/tester:
   https://regex101.com/
2. Regular Expressions for overlapping substring search:
   https://www.geeksforgeeks.org/python-program-to-find-indices-of-overlapping-substrings/
3. "Positive Lookahead" regular expression:
   https://www.rexegg.com/regex-lookarounds.html
"""
