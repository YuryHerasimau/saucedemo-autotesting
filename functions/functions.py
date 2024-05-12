def sort_list_by_price(lst: list, reverse_value: bool):
    # clean_list = [float(i.replace("$", "")) for i in lst]
    # return sorted(clean_list, reverse=reverse_value)
    return sorted(lst, key=lambda i: float(i.replace("$", "")), reverse=reverse_value)


def sort_list_by_name(lst: list, reverse_value: bool):
    return sorted(lst, reverse=reverse_value)
