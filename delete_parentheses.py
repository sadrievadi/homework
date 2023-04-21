def delete_parentheses(sentence):
    index_pair_list = []
    left = 0
    while left < len(sentence):
        if sentence[left] == '(':
            right = left
            open_cnt = 1
            while open_cnt > 0:
                right += 1
                if sentence[right] == ')':
                    open_cnt -= 1
                elif sentence[right] == '(':
                    open_cnt += 1
            index_pair_list.append((left, right))
            left = right + 1
        else:
            left += 1
    result = ""
    last_left = 0
    for p in index_pair_list:
        left, right = p
        if left > 0:
            result += sentence[last_left:left]
        last_left = right + 1
    if last_left < len(sentence) - 1:
        result += sentence[last_left:]
    return result


print(delete_parentheses("(fdsf)dskf(fds)"))
print(delete_parentheses("(fdsfdskffds)"))
print(delete_parentheses("(fds)(fdsfdskffds)(fdsfsdf)"))
print(delete_parentheses("sdfsd((fds)(fdsfdskffds)(fdsfsdf))fdskdljsjk"))