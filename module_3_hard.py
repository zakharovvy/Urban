
def calculate_structure_sum (args) -> int:
    result_1 = 0
    if isinstance (args, int):
        result_1 += args
    elif isinstance (args, float):
        result_1 += args
    elif isinstance(args, str):
        result_1 += len(args)
    elif isinstance(args, (list, tuple, set)):
        for i in args:
            result_1 += calculate_structure_sum(i)
    elif isinstance(args, dict):
        for key, value in args.items ():
            result_1 += calculate_structure_sum(value)
            result_1 += calculate_structure_sum(key)

    return result_1

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
