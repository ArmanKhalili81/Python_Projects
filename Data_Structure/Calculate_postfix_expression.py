from Stack import Stack

# ----------------------------------------------------------------------------------\
def main(data):
    st = Stack()
    postfix_exp = data
    test_expression = True  # for check that if expression is postfix or not ?

    for index in range(len(postfix_exp)):
        if postfix_exp[index].isdigit():
            st.push(int(postfix_exp[index]))
        else:
            match postfix_exp[index]:
                case '+':
                    num1 = st.pop()
                    num2 = st.pop()
                    sum_res = num1 + num2
                    st.push(sum_res)
                case '-':
                    num1 = st.pop()
                    num2 = st.pop()
                    min_res = num2 - num1
                    st.push(min_res)
                case '*':
                    num1 = st.pop()
                    num2 = st.pop()
                    mul_res = num1 * num2
                    st.push(mul_res)
                case '/':
                    num1 = st.pop()
                    num2 = st.pop()
                    div_res = num2 / num1
                    st.push(div_res)

                case _:
                    test_expression = False
                    break

    if test_expression:
        print(f"Result : {st.pop()}")

    else:
        from os import system
        system(f"msg * {postfix_exp} isn't PostFix !")

    """
    2 3 - 4 + 5 6 7 * + *
    3 4 2 - * 5 *
    3 4 * 2 5 * +
    2 3 4 * +
    4 6 * 5 ! 2 9 @
    """
