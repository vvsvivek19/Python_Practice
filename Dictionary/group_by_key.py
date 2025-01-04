from collections import defaultdict
example_list = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
example_dict = defaultdict(list)

for alpha,numb in example_list:
    example_dict[alpha].append(numb)

print(example_dict)