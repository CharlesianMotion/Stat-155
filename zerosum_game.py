'''def joshcry(lst):
    p1 = lst[0]
    p2 = lst[1]
    v1 =        8*p1 + 4*p2
    v2 = 3           + 4*p2
    v3 = 8    - 4*p1 - 7*p2
    v4 = 5    - 4*p1 +   p2
    print(v1,v2,v3,v4)
    return min(v1,v2,v3,v4)
n = 1000
# wan = [i/n for i in range(n+1)]

def sq_set(wan):
    sq_wan = []
    for i in wan:
        for j in wan[:n+1-int(n*i)]:
            sq_wan.append([i,j])
    return sq_wan



n1 = 0.3229167
n2 = 0.3750000
m = 400

# a = max(josh_sq, key = joshcry)
# 0.323 0.375

sherman1 = [n1+ i/100000000 for i in range(-m,m)]

sherman2 = [n2+ i/100000000 for i in range(-m,m)]

wan2sq = []
for i in sherman1:
    for j in sherman2:
        wan2sq.append([i,j])

# print(wan2sq)
b = max(wan2sq, key = joshcry)
print(b)
print(sherman1)
'''
'''
def guess_frac(n = 0.322917, rangee = 100, decimals = 6):
    lst = []
    for j in range(1,rangee//2):
        for i in range(2*j+1,rangee):
            if round(i/j,decimals) == n:
                lst.append([i,j,i/j])
    print(lst)
    return lst

joshcry([31/96,3/8])

guess_frac(4.083333)

def joshcry2(lst):
    q1 = lst[0]
    q2 = lst[1]
    q3 = lst[2]
    q4 = 1-q1-q2-q3
    v1 = 8*q1+3*q2+4*q3+q4
    v2 = 4*q1+7*q2+q3+6*q4
    v3 = 3*q2+8*q3+5*q4
    
    return max(v1,v2,v3)

#wan3 = [i/100 for i in range(101)]

wan3_s = []



n1 = 0.32223
n2 = 0.03300
n3 = 0.25825
m  = 100

sherman1 = [n1+ i/100000 for i in range(-m,m)]

sherman2 = [n2+ i/100000 for i in range(-m,m)]

sherman3 = [n3+ i/100000 for i in range(-m,m)]

for i in sherman1:
    for j in sherman2:
        for k in sherman3:
            wan3_s.append([i,j,k])

c = min(wan3_s, key = joshcry2)

print(1-0.322-0.033-0.258)
'''

#def zerosum(lst, nrow):


from itertools import product

def solve_zero_sum_game(lst, nrow, layer = 7, indicator = 1):
    half_total_n = 14
    step = 1e-2
    layer = 7
    current_layer_done = 1


    ncol = len(lst)//nrow
    dic_of_para = {i:[lst[k*ncol+i] for k in range(nrow)]for i in range(ncol)}
    # has ncol keys, every key has nrow parameters.
    #print(dic_of_para)

    

    #print(create_list_of_p1(0.12))

    def core_function(p):
        '''p is a list. p means a vector containing p1, p2, p3, ..., pn
        It returns a min of the list of Vs.
        '''
        lst = []
        for i in range(ncol):
            lst.append(sum([para*pi for para, pi in zip(dic_of_para[i],p)]))
        return min(lst)

    hundred = [0.1*i for i in range(11)]
    the_first_p_vectors_unfinished = product(hundred, repeat = nrow)
    the_first_p_vectors = [element for element in the_first_p_vectors_unfinished if sum(element) < 1+1e-12 and sum(element) > 1-1e-12]
    est_p_vector = max(the_first_p_vectors, key = core_function)
    #print(est_p_vector)

    def create_list_of_pi(est_pi):
        """est_pi is one element of the vector p.
        We use this function to create multiple pi's around the estimated pi, 
        which is an element of the estimated vector p.
        """
        return [est_pi + i*step for i in range(-half_total_n, half_total_n) if est_pi+i*step >= 0-1e-12 and est_pi+i*step <=1+1e-12]
    

    def create_new_p_vectors(est_p_vector):
        unfinished = create_list_of_pi(est_p_vector[0])
        
        k = 1
        while k < nrow:
            if k == 1:
                unfinished = [ [i] + [j] for i in create_list_of_pi(est_p_vector[0]) for j in create_list_of_pi(est_p_vector[1])]
            else:
                unfinished = [ i + [j] for i in unfinished for j in create_list_of_pi(est_p_vector[k])]
            k+=1

        finished = [i for i in unfinished if sum(i) <= 1+1e-12 and sum(i) >= -1e-12]
        return finished



    while current_layer_done < layer:
        

        candidate_p_vectors = create_new_p_vectors(est_p_vector)
        
        est_p_vector = max(candidate_p_vectors, key = core_function)
        current_layer_done += 1
        step = step/10


    
    if indicator == 1:

        def reverse_matrix(lst,nrow):
            ncol = len(lst)//nrow
            result = []
            for i in range(ncol):
                for j in range(nrow):
                    result.append(-lst[i+j*ncol])
            return result

        reverse_lst = reverse_matrix(lst,nrow)

        q_strategy = solve_zero_sum_game(reverse_lst,ncol,layer,0)

        return (est_p_vector,q_strategy)
    

    return est_p_vector



def flo_vec_to_frac(tupl):
    result_lst1, result_lst2 = [], []
    lst1, lst2 = tupl[0], tupl[1]
    for flo in lst1:
        result_lst1 += [flo_to_frac(flo)]
    for flo in lst2:
        result_lst2 += [flo_to_frac(flo)]   
    return result_lst1, result_lst2




def flo_to_frac(flo):
    for x in range(100):
        for y in range(1,100):
            if abs(x/y-flo) <= 1e-4:
                if abs(x/y-flo) <= 1e-6:
                    print(abs(x/y-flo))
                return "{0}/{1}".format(x,y)
    return "nothing we found"




matrix = [2,-3,2,3,0,-1,-2,1,0]
print(solve_zero_sum_game(lst = matrix, nrow = 3))

'''
def reverse_matrix(lst,nrow):
    ncol = len(lst)//nrow
    result = []
    for i in range(ncol):
        for j in range(nrow):
            result.append(-lst[i+j*ncol])
    return result

q_matr = reverse_matrix(matrix,3)

print(solve_zero_sum_game(lst = q_matr, nrow = 4))
'''














