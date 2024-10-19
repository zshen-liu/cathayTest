def correct_number(n):
    """

    :param n: incorrect number
    :return: rel_up_down and rel avg
    """
    incorrect_up_down = [i for i in range(n - 3, n + 4)]
    correct_up_down = []
    for number in incorrect_up_down:
        #revverse the number
        value = int(str(number)[::-1])
        if 0 <= value <= 100:
            correct_up_down.append(value)
    avg_up_down = int(sum(correct_up_down) / len(correct_up_down))
    return correct_up_down, avg_up_down


rel_up_down,rel_avg = correct_number(42)
print(f'可能實際漲跌幅 {rel_up_down}')
print(f'平均實際漲跌幅 {rel_avg}')
