def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    if len(input) <= 1:
        return True
    
    first_char = input[0]
    last_char = input[-1]
    
    if first_char is not last_char:
        return False
    
    remaining = input[1:-1]
    return is_palindrome(remaining)
        

# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
