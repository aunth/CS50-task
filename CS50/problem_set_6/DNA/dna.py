import csv
import sys


def main():
    if len(sys.argv) != 3:
        return "Usage: python3 dna.py data.csv sequence.txt"
    file1 = open(sys.argv[1])
    title = file1.readline()
    database = csv.reader(file1)
    file2 = open(sys.argv[2])
    DNA = file2.read()
    genome = [str(longest_match(DNA, i)) for i in title.strip().split(',')[1:]]
    print(genome)
    for i in database:
        if i[1:] == genome:
            return i[0]
    file1.close(); file2.close()
    return "No match"


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


print(main())
