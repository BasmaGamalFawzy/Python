## I used VS Code + Github Copilot for autocomplete + Gemini NotebookLM for explaining some concepts from the Lectures ###

# 2) Write a program that computes the power set of the set {1,2,…,𝑛}, with 𝑛≤10. 
# The program reads 𝑛, then lists all the subsets of {1,2,…,𝑛}.
# For example: for 𝑛=3, the output is: {𝜙,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}


def main():

    # Use a Validation loop to ensure correct input for n is between 1 and 10
    while True:
        try:
            n = int(input("Enter size of the set (1 <= n <= 10): "))
            if 1 <= n <= 10:
                break
            print("Set size n must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")

            
    subsets = []

    # Generate all 2^n subsets using bit masking
    for i in range(1 << n):
        subset = [j + 1 for j in range(n) if (i >> j) & 1]
        subsets.append("{" + ",".join(map(str, subset)) + "}" if subset else "ϕ")

    print("\nPower Set:")
    print("{" + ", ".join(subsets) + "}")
    print(f"Total subsets: {len(subsets)}")

    input("\nPress Enter to exit...")
    

# Calling main in a safe way to ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
