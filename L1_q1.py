## I used VS Code + Github Copilot for autocomplete + Gemini NotebookLM for explaining some concepts from the Lectures ###


# 1) Write a program that presents a menu of 3 options:
#   a) Compute the union of two sets
#   b) Compute the intersection of two sets
#   c) Compute the complement of a set
# The sets are all understood as subsets of a universal set 𝑈={1,2,3…,𝑛},
# with 𝑛≤20. For example, if 𝑛=7, the elements of the set {4,2,5} are entered one by one, as integers, and 
# the set is then represented internally as the bit string: 0 1 0 1 1 0 0
# The output of the program is the list of elements (as integers) of the requested set

def read_set_bits(name, n):
    # read the elements of a set, split by spaces, and return its values as string list
    elements = input(f"Enter elements of set {name} (space-separated integers): ").split()
    # Initialize a bit string of length n with all bits set to 0
    bits = [0] * n
    # Loop through the entered elements and set the corresponding bits to 1
    for x in elements:
        # Check if the entered element is a valid integer and within the range of the universal set
        if x.isdigit() and 1 <= int(x) <= n:
            # Set the bit corresponding to the element to 1 (subtract 1 as bits array is zero-based indexed)
            bits[int(x) - 1] = 1
    return bits

def print_set_bits(bits):
    # Print the bit string representation of the set
    print("\nBit string:", " ".join(map(str, bits)))
    # Print the actual elements of the set based on the bit string
    print("Set elements:", [i + 1 for i in range(len(bits)) if bits[i] == 1])

def main():

    # Use a Validation loop to ensure correct input for n is between 1 and 10
    while True:
        try:
            n = int(input("Enter universal set size n (1-20):"))
            if 1 <= n <= 20:
                break
            print("Set size n must be between 1 and 20.")
        except ValueError:
            print("Please enter a valid integer.")
            
    
    print("Choose an option \na) Union  b) Intersection  c) Complement")
    choice = input("Choose option (a/b/c): ").strip().lower()

    # Union
    if choice == 'a':
        a = read_set_bits("A", n)
        b = read_set_bits("B", n)
        # either a or b is 1, then the result is 1, otherwise 0
        res_bits = [a[i] | b[i] for i in range(n)]
        print_set_bits(res_bits)
            

    # Intersection
    elif choice == 'b':
        a = read_set_bits("A", n)
        b = read_set_bits("B", n)
        # both a and b are 1, then the result is 1, otherwise 0
        res_bits = [a[i] & b[i] for i in range(n)]
        print_set_bits(res_bits)

    elif choice == 'c':
        a = read_set_bits("A", n)
        # if a is 1, then the result is 0, otherwise 1
        res_bits = [1 - a[i] for i in range(n)]
        print_set_bits(res_bits)

    input("\nPress Enter to exit...")
    

# Calling main in a safe way to ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
