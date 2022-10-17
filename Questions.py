def truth_question(t_q):
    if len(t_q)>0:
        from random import randint
        x=randint(0,(len(t_q)-1))
        z=str(t_q[x])
        t_q.pop(x)
        return(z)
    else:
        return("Out of Questions")

def dare_question(d_q):
    if len(d_q)>0:
        from random import randint
        x=randint(0,(len(d_q)-1))
        z=str(d_q[x])
        d_q.pop(x)
        return(z)
    else:
        return("Out of Dares")

