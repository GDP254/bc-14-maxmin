
def find_max_min(lst):
    print "Use inbuilt max function to get the largest number in the list"
    ma = max(lst)
    print "Use inbuilt min function to get the smallest number in the list"
    mi = min(lst)
    print "If the values obtained are equal:"
    print "     present the max value as a single value in an array"
    print "else:"
    print "     present the min and max value as the first and second items respectively in an array"
    if ma == mi:
        return [ma]
    else:
        return [mi, ma]