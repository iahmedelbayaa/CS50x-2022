import csv
import re
from sys import argv, exit


if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

with open(argv[1], newline="") as csvfile:
    database_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for i, row in enumerate(database_reader):
        if i == 0:
            with open(argv[2], "r") as txtfile:
                line = next(txtfile)
                longest_strs = []
                for i in range(1, len(row)):
                    pattern = row[i]
                    matches = (
                        match[0] for match in re.finditer(fr"(?:{pattern})+", line)
                    )
                    try:
                        longest = int(len(max(matches, key=len)) / len(pattern))
                        longest_strs.append(longest)
                    except ValueError:
                        longest_strs.append(0)
        else:
            list_database_strs = list(map(int, row[1:]))
            if list_database_strs == longest_strs:
                print(row[0])
                break
    else:
        print("No match")

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


main()
