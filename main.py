import itertools

#Q create a function that returns True if there is a sum of 2 numbers with the value 10

#lesson1
#best
# O(n) time | O(n) space
def existsTwoNumberSumFast(array,targetSum):
    h = set() # hashset
    for i in range(len(array)): #Time: O(n), Space: O(n)
        y = targetSum - array[i]
        if y in h: #O(1)
            #print (a[i],y)
            #return True
            return [array[i],y]
        h.add(array[i]) #Space: O(n)
    return []

#best2!
# O(nlog(n)) time | O(1) space
def existsTwoNumberSumSorted(a,s):
    #a = sorted(a) #time: O(nlogn), #space: O(1)
    a.sort()
    l = len(a)
    if l<2:
        return []
    
    L = 0 ; R = l-1 #pointers

    while(L < R):
        if a[L]+a[R]==s:
            return [a[L],a[R]]
        
        if a[L]+a[R]<s:
            L+=1
        else: #a[L]+a[R]>s
            R-=1
    return []

#Classic
def existsTwoNumberSum(a, s):
    l = len(a)
    for i in range(l): #time: O(n^2), space: O(1)
        for j in range(i+1,l):
            if a[i]+a[j] == s:
                return [a[i],a[j]]
    return []



#Full pythonian
def existsTwoNumberSum2(a, s):
    #return any(True for c in ((a[i],a[j]) for i in range(0,len(a)-1) for j in range(i+1,len(a))) if c[0]+c[1]==s)
    l = len(a)
    return any(c[0]+c[1]==s for c in ((a[i],a[j]) for i in range(0,l-1) for j in range(i+1,l)))

a = [ 3,5,-4,8,11,1,-1,6]
target_sum = 10

#print(existsTwoNumberSum(a,target_sum))
#print(existsTwoNumberSum2(a,target_sum))
print(existsTwoNumberSumFast(a,target_sum))
print(existsTwoNumberSumSorted(a,target_sum))


# #1st way
# combos = itertools.combinations(a,2)
# for c in combos:
#     if sum(c) == s_target:
#         print(c)


#combos = [i for i in range(0,len(a))] #εδώ δεν θέλει list()
#combos = (i for i in range(0,len(a))) #generator (preferred)
#combos = [[(a[i],a[j]) for j in range(0,len(a)) if j>i] for i in range(0,len(a))] #test

#2nd way
#list_1D = [item for sub_list in list_2D for item in sub_list]
combos = ((a[i],a[j]) for i in range(0,len(a)-1) for j in range(i+1,len(a))) #in nested we write the 'for' in reverse
#[(3, 5), (3, -4), (3, 8), (3, 11), (3, 1), (3, -1), (3, 6), (5, -4), (5, 8), (5, 11), (5, 1), (5, -1), (5, 6), (-4, 8), (-4, 11), (-4, 1), (-4, -1), (-4, 6), (8, 11), (8, 1), (8, -1), (8, 6), (11, 1), (11, -1), (11, 6), (1, -1), (1, 6), (-1, 6)]
#combos_with_sum = list(filter(lambda c: c[0]+c[1]==10,combos))
combos_with_sum  = any(c for c in combos if c[0]+c[1]==target_sum)
#print(combos_with_sum)







