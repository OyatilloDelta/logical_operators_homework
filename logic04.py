def main(a,b):
    """
    Given two integers a, b,  check the following statement "C".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x1=a%2==0
    x2=b%2==0
    return x1 and x2 
print(main(4,6))