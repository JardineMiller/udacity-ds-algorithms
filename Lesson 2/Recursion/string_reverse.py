# Code

def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    

    if len(input) == 0:
        return ""

    first_char = input[0]
    remaining = input[slice(1, None)]
    reverse = reverse_string(remaining)
    reverse += first_char
    return reverse

# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")