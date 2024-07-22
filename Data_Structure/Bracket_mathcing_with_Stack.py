from Stack import Stack

def check_bracket(statement):
    st = Stack()
    ls1 = ['(','{','[']
    ls2 = [')','}',']']
    for s in statement :
        if s in ls1 :
            st.push(s)
        elif s in ls2 :
            item = st.pop()
            if item is ls1[0] and s is ls2[0]:
                continue
            elif item is ls1[1] and s is ls2[1]:
                continue
            elif item is ls1[2] and s is ls2[2]:
                continue
            else :
                return False
    if st.size > 0 :
        return False
    else :
        return True

s1 = (
"{(foo)(bar)}[hello](((this)is)a)test",
"{(foo)(bar)}[hello](((this)is)atest",
"{(foo)(bar)}[hello](((this)is)a)test))"
)
for ch in s1 :
    res = check_bracket(ch)
    print("Statement : {0} , Result Of Check : {1}".format(ch,res))