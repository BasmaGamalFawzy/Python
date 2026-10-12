## I used VS Code + Github Copilot for autocomplete + Gemini NotebookLM for explaining some concepts from the Lectures ###

# 3) Write a program that presents a menu of 3 options:
#   a) Compute the union of two relations 𝑅1∪𝑅2 on a set 𝐴
#   b) Compute the composite of two relations 𝑅1𝑜𝑅2 on a set 𝐴
#   c) Compute the transitive closure of a relation on 𝐴: 𝑅∗


def read_matrix(name, n):
    print(f"\nEnter {n}x{n} Boolean matrix for {name} row by row (0s and 1s only) each bit is space-separated:")
    matrix = []
    # loop to take the inputs row by row
    for i in range(n):
        # For each row ensure correct input: accepts only 0s and 1s
        while True:
            # Take input, split by spaces, and strip whitespace & store them in a list of strings
            vals = input(f"Row {i+1}: ").strip().split()
            # Check if the number of values is equal to n and all values are either '0' or '1'
            if len(vals) == n and all(v in ('0', '1') for v in vals):
                # Convert the list of strings to a list of integers and append to the matrix
                matrix.append([int(v) for v in vals])
                break
            print(f"Invalid input! Please enter exactly {n} values, each being 0 or 1.")
    return matrix

def print_matrix(M, title):
    print(f"\n{title}:")
    for row in M:
        print(*row)

def main():
    # Ensure correct input for n is between 1 and 10
    while True:
        try:
            n = int(input("Enter size of set A (1 <= n <= 10): "))
            if 1 <= n <= 10:
                break
            print("Set size n must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")

    # Present the menu of options
    print("\na) Union (R1 U R2)")
    print("b) Composite (R1 o R2)")
    print("c) Transitive Closure (R*)")
    choice = input("Choose option (a/b/c): ").strip().lower()

    # Union
    if choice == 'a':
        R1 = read_matrix("R1", n)
        R2 = read_matrix("R2", n)
        # loop through each element of the two matrices and compute the union using their logical OR
        union = [[R1[i][j] | R2[i][j] for j in range(n)] for i in range(n)]
        print_matrix(union, "Union Matrix (R1 U R2)")

    # Composite
    elif choice == 'b':
        R1 = read_matrix("R1", n)
        R2 = read_matrix("R2", n)
        # Composite R1 o R2 corresponds to Boolean product M_R2 x M_R1
        comp = [[1 if any(R2[i][k] and R1[k][j] for k in range(n)) else 0 for j in range(n)] for i in range(n)]
        print_matrix(comp, "Composite Matrix (R1 o R2)")

    # Transitive Closure
    elif choice == 'c':
        R = read_matrix("R", n)
        # Create a copy of R to W for the transitive closure computation
        W = [row[:] for row in R]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    #  Update W[i][j] to include the transitive closure using the Floyd-Warshall algorithm
                    W[i][j] |= (W[i][k] & W[k][j])
        print_matrix(W, "Transitive Closure Matrix (R*)")

    else:
        print("Invalid choice selected.")

    input("\nPress Enter to exit...")

# Calling main in a safe way to ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
