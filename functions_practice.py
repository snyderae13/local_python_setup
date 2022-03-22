def hello():
    print("Hello, user!")

def pack(a, b, c):
    return [a,b,c]

def eat_lunch(lunch_lst):
    if len(lunch_lst) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch_lst)):
            if i == 0:
                print(f"First I eat {lunch_lst[0]}")
            else:
                print(f"Next I eat {lunch_lst[i]}")


hello()
print(pack("a", "b", "c"))
eat_lunch([])
eat_lunch(["sauerkraut"])
eat_lunch(["herring roll-up", "bratwurst", "kringle"])

