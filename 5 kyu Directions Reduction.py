arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]  # []


def dir_reduc(arr):
    pop_list = []
    for i in range(len(arr) - 1):
        if len(pop_list) > 0:
            i = 0
        if len(arr) - 1 <= 0:
            break
        if (
            (arr[i] == "NORTH" and arr[i + 1] == "SOUTH")
            or (arr[i] == "SOUTH" and arr[i + 1] == "NORTH")
            or (arr[i] == "EAST" and arr[i + 1] == "WEST")
            or (arr[i] == "WEST" and arr[i + 1] == "EAST")
        ):
            if (i + 1) == len(arr) - 1:
                pop_list.append(arr.pop(i))
                arr.pop(i)
                return arr
            else:
                pop_list.append(arr.pop(i))
                arr.pop(i)
                dir_reduc(arr)
    return arr


# print(range(len(arr)))
print(dir_reduc(arr))
