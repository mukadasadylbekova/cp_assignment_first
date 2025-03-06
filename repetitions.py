dna = input().strip()

max_length = 1
current_length = 1

for i in range(1, len(dna)):
    if dna[i] == dna[i - 1]:
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1  # Reset for new character

max_length = max(max_length, current_length)  # Final update
print(max_length)
