"""Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

S
e
r
i
e
s
:
1
+
1
4
+
1
7
+
1
10
+
1
13
+
1
16
+
…
Series:1+
4
1
​
 +
7
1
​
 +
10
1
​
 +
13
1
​
 +
16
1
​
 +…
You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

Examples (Input --> Output)
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"""


def series_sum(n):
    if n == 0:
        return "0.00"
    else:
        result = 1
        i = 4
        for _ in range(1, n):
            result += 1 / i
            i += 3
        s = str(round(float(result), 2))
        if len(s) < 4:
            s += "0"
        return s
