lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

has_no_consecutive_ones = lambda line: line.count('11') == 0

valid_sequences_count = sum(1 for line in lines if has_no_consecutive_ones(line))

print(f"Ilość ciągów niezawierających dwóch sąsiadujących jedynek: {valid_sequences_count}")
