from Stack import Stack
import Calculate_postfix_expression


def precedence(operator):
    if operator == "/" or operator == "*":
        return 3
    elif operator == "+" or operator == "-":
        return 2
    else:
        return 1


st = Stack()
in_exp = input()
post_exp = ""

for tmp in in_exp:
    if tmp.isdigit():
        post_exp += tmp
    elif tmp == "+" or tmp == "-" or tmp == "*" or tmp == "/":
        if st.peek() == "(":
            st.push(tmp)
        else:
            if precedence(tmp) > precedence(st.peek()):
                st.push(tmp)
            elif precedence(tmp) < precedence(st.peek()):
                post_exp += st.pop()
                st.push(tmp)
            else:
                post_exp += st.pop()
                st.push(tmp)
    elif tmp == "(":
        st.push(tmp)
    elif tmp == ")":
        while st.peek() != "(":
            post_exp += st.pop()
        st.pop()

while st.size > 0:
    post_exp += st.pop()
print("----------------------------------------------------")
print("After Convert To Postfix : {0}".format(post_exp))
Calculate_postfix_expression.main(post_exp)
