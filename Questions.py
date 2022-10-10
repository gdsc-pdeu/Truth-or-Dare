def truth_question(t_q):
    from random import randint
    x=randint(0,(len(t_q)-1))
    z=str(t_q[x])
    t_q.pop(x)
    return(z)

def dare_question(d_q):
    from random import randint
    x=randint(0,(len(d_q)-1))
    z=str(d_q[x])
    d_q.pop(x)
    return(z)

