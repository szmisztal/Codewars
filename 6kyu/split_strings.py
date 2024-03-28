"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""


def solution(s):
    s_split = list(s)
    result = []
    if len(s) % 2 == 0:
        for i in range(1, len(s_split), 2):
            result.append(s_split[i - 1] + s_split[i])
    else:
        for i in range(1, len(s_split) - 1, 2):
            result.append(s_split[i - 1] + s_split[i])
        result.append(s_split[-1] + "_")
    return result
