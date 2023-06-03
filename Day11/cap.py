def capitalize_list_items(value):
    cap = list()
    for i in value:
        cap.append(i.upper())
    return cap

print(capitalize_list_items(["a", "b", "c"]))