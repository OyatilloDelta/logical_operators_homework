def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    j=a//100
    s=a%100
    d=s//10
    t=s%10
    l=(d+t+j)==0
    return l
print(main(222))