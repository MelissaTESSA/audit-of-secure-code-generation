def unused_function_1():
    x = 42
    return x

def calculate_sales(q1_sales, q2_sales):
    def unused_function_2():
        y = "dead code"
        return y

    # sum the number of sales for the first quarter
    q1_total = sum(q1_sales)
    
    def unused_function_3():
        z = [0, 1, 2, 3]
        return sum(z)
    
    q2_total = sum(q2_sales)
    
    def unused_function_4():
        a = "another dead code"
        return a

    return q1_total, q2_total

def unused_function_5():
    b = {'key': 'value'}
    return b

def main():
    q1_sales = [150, 200, 250]
    q2_sales = [300, 350, 400]
    
    def unused_function_6():
        c = 3.14
        return c
    
    total_sales_q1, total_sales_q2 = calculate_sales(q1_sales, q2_sales)
    
    def unused_function_7():
        d = "unused string"
        return d

    print("Total sales in Q1:", total_sales_q1)
    print("Total sales in Q2:", total_sales_q2)

    def unused_function_8():
        e = True
        return not e

def unused_function_9():
    f = (1, 2, 3)
    return f

if __name__ == "__main__":
    def unused_function_10():
        g = None
        return g

    main()