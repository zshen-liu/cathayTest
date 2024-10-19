def gen_number_list(n):
    """

    :param n: target number
    :return: the records for the target number in list
    """
    if n < 1:
        return []
    # initial first and second number
    result = [0, 1]
    for i in range(2, n):
        value = result[i - 1] * (result[i - 2] + 1)
        result.append(value)
    return result


def find_number(target):
    """

    :param target: target number
    :return: less than equal target number on list and index number
    """
    # initial first and second number
    target_result_list = [0, 1]
    # start calculate from index 2
    index = 2
    while True:
        value = target_result_list[index - 1] * (target_result_list[index - 2] + 1)
        # break if value over target
        if value >= target:
            break
        target_result_list.append(value)
        index += 1

    return target_result_list[-1], index


n = 13
print(f"前 {n} 項: {gen_number_list(n)}")
limit = 1000
number, index = find_number(limit)
print(f"小於 {limit} 的最大數為: {number}，位於第 {index} 項")
