
def genstable_e(l, ss, g):
    '''
    Use to generate a stable e value given values for l, ss, and g
    '''
    return (-(l-1)*((g-1)*ss+1))/(g)


def genstable_g(l,ss,e):
    '''
    Use to generate a stable g value given values for l, ss, and e
    '''
    return (float(l)-1)*(float(ss)-1)/((float(l)-1)*float(ss)+float(e))

def genstable_ss(l,g,e):
    '''
    Use to generate a stable ss value given values for l, g, and e
    '''
    return (-(e*g+l-1))/((g-1)*(l-1))
    
def genstable_l(ss,g,e):
    '''
    Use to generate a stable l value given values for ss, g, and e
    '''
    return 1-(float(e)*float(g))/((float(g)-1)*float(ss)+1)