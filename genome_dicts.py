# Dictionary for a Genome statistics
from random import choice
from collections import defaultdict

genome_size = 12
genome = "AGATCGGTCGGAGAGA"
#genome = ''.join([choice("ATCG") for nuc in range(genome_size)])

print(genome)

# -----------

# genome_dict = {}
k = 3

#genome_dict['ATT'] = [2, 3]
#genome_dict['ATA'] = 2

# for x in range(len(genome) - k + 1):
#     kmer = genome[x:x + k]
#     if kmer in genome_dict:
#         genome_dict[kmer].append(x)
#     else:
#         genome_dict[kmer] = [x]


# -----------


genome_dict = defaultdict(list)

for x in range(len(genome) - k + 1):
    kmer = genome[x:x + k]
    genome_dict[kmer].append(x)

# Printing:
for key, value in genome_dict.items():
    print(key, value)
