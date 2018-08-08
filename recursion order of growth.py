def powerSet(L):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(L) == 0:
        # If the list is empty, return the empty list
        return [[]]
    ps = []
    first = L[0]
    rest = L[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for e in powerSet(rest):
        print ps
        ps.append(e)
        
        next_subset = e + [first]
        ps.append(next_subset)
        print ps
    return ps


L = [1,2,3,4]
#Q = powerSet(L)
#print Q
e = []
f = 5
L.append(e+[f])
print L