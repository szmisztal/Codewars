"""There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required."""


def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    elif n > len(customers):
        return max(customers)
    else:
        tills = customers[:n]
        for i in tills:
            customers.remove(i)
        while len(customers) > 0:
            idx = tills.index(min(tills))
            tills[idx] += customers[0]
            customers = customers[1:]
        return max(tills)



