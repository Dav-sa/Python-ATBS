spam = ["apples", "bananas", "tofu", "cats"]
spam2 = []


def commaCode(list):
    if not list:
        print("list is empty")
        return
    return " ,".join(list[0:-2]) + " " + "and " + str(list[-1])


print(commaCode(spam))
