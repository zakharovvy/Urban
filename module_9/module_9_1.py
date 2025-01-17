#Я так понимаю, что функции max, min и некоторые другие расписывать не надо, так как они уже встроены в Python
def apply_all_func(int_list:list, *functions):
    results = {}
    for function in functions:
        func_result = function(int_list)
        results[str(function.__name__)] = func_result
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))