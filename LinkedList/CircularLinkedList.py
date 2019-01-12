from singleLinke import SingleNode


def reverse_between(link, f, t):
    f_node = link.__head
    pre_f = find_pre_node(f_node,f)
    pre_t = find_pre_node(f_node,t)
    f_next = f.next
    t_next = t.next
    pre_f.next = t
    if t.next ==None:
        f.next == None
    else:
        f.next = t_next
    
    pre_t.next =f


    


def find_pre_node(f_node,f):
    while f_node:
        pre = f
        node = f_node.next
        if node == f:
            return pre

