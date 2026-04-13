

import sys

def text_to_machine_code():
    print("=== Text to Machine Code (Binary Format) ===")
    user_input = input("Enter text: ")
    
    if not user_input:
        print("Error: Input is empty.")
        return

    print(f"\nAnalysis for: '{user_input}'")
    print("-" * 50)
    print(f"{'Char':<8} | {'Dec':<10} | {'Binary (8-bit)':<20}")
    print("-" * 50)

    binary_result = []

    for char in user_input:
        decimal_val = ord(char)
        binary_val = format(decimal_val, '08b')
        
        print(f"{char:<8} | {decimal_val:<10} | {binary_val:<20}")
        binary_result.append(binary_val)

    print("-" * 50)
    print("\nFull Machine Code:")
    print(" ".join(binary_result))
    print("-" * 50)

if __name__ == "__main__":
    try:
        text_to_machine_code()
    except KeyboardInterrupt:
        sys.exit()
