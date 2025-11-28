import random
import string
import time

# Dictionary to map screen size choice to the blocks to generate per line
# '1080p': The original 13 blocks
# '2k': 20 blocks
# 'mac': 26 blocks (Corrected key and value)
# '4k': 30 blocks
BLOCK_COUNTS = {
    '1080p': 13,
    '2k': 20,
    'mac': 26,  # Corrected key from '23' to 'mac' and value for consistency with prompt
    '4k': 30
}

def get_block_count():
    print("\nSelect an output density (Screen Size):")
    print("  1. 1080p (13 blocks per line - Standard)")
    print("  2. 2K (20 blocks per line - Higher density)")
    print("  3. Mac (26 blocks per line - Dev Standard)")
    print("  4. 4K (30 blocks per line - Very high density)")
    
    while True:
        # Added 'mac' to the list of expected inputs
        choice = input("Enter your choice (1, 2, 3, 4, 1080p, 2k, mac, or 4k): ").lower().strip()

        if choice in ['1', '1080p']:
            return BLOCK_COUNTS['1080p']
        elif choice in ['2', '2k']:
            return BLOCK_COUNTS['2k']
        # Corrected the logic for the 'Mac' option (choice 3)
        elif choice in ['3', 'mac']:
            return BLOCK_COUNTS['mac']
        # Added logic for '4K' option (choice 4)
        elif choice in ['4', '4k']:
            return BLOCK_COUNTS['4k']
        else:
            # Updated prompt to reflect all valid single-digit choices
            print("Invalid choice. Please enter 1, 2, 3, 4, 1080p, 2k, mac, or 4k.")

def letterprint(num_blocks):
    print(f"\n--- Generating {num_blocks} blocks per line. Press Ctrl+C to stop. ---")

    while True:
        # List comprehension to generate blocks
        # Each block is a shuffled string of 26 lowercase alphabet letters
        blocks = [
            ''.join(random.sample(string.ascii_lowercase, 26))
            for _ in range(num_blocks)
        ]

        # Print all blocks separated by spaces
        print(*blocks)

        sleep()

def sleep():
    # It's generally better to use a variable for sleep time if it might change
    # But keeping it simple as per the original structure
    time.sleep(0.3)

def main():
    block_count = get_block_count()

    try:
        letterprint(block_count)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()











































