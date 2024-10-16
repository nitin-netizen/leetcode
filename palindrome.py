def is_palindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert the number to a string
    x_str = str(x)
    
    # Compare the string with its reverse
    return x_str == x_str[::-1]

