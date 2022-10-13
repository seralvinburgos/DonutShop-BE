

# LISTS
def list_1():
    print("List 1")

    colors = ["red", "green", "blue"]
    print(colors)
    print(type(colors))

    # add element
    colors.append("white")

    # count / length
    print(len(colors))


    # delete
    # by index
    del colors[0]

    # by value
    colors.remove("white")


    # travel a list
    for color in colors:
        print(color)

def list_2():
    print("List 2")
    nums = [12,34,-1,53,12,88,55,32,-123,9,1,78,1,-4,11,5,6,4,678,4,883,0, -13, 12, 92]

    # print all numbers that are greater
    for n in nums:
        if n < 0:
            print(n)

    # print the sum of all numbers
    # count numbers greater than 50
    # count numbers between 10 and 50
    total = 0
    count = 0
    between = 0
    for num in nums:
        total = total + num

        if num > 50:
            count += 1

        if num >= 10 and num <= 50:
            between += 1


    print(total)
    print("There are " + str(count) + " numbers greater than 50") # There are  numbers than 50
    print("There are " + str(between) + " numbers between 10 and 50")


# Dictionary

def dict_1():
     
    me = {
        "name" : "Alvin",
        "last" : "Burgos",
        "age" : 40,
        "hobbies" : [],
        "address" : {
            "street" : "Baker",
            "num" : "22B",
            "city" : "Marylebone",
            "zip" : "W1U 3BW"
        }
     }

    print(me)
    print(type(me))


    # add pairs
    me["preferred_color"] = "blue"

    # modify
    me["age"] = 99

    # delete key
    del me["hobbies"]

    print(me)

    # read
    name = me["name"]
    print(name)

    # print the address in the following format:
    # street #, city, zip
    # print(me["address"]["street"] + " " + me["address"]["num"]
    
    address = me["address"]
    print(address["street"] + " " + address["num"] + ", " + address["city"] + ", " + address["zip"])

    # f string
    # print(f"{address['street']} {address['num']}, {address['city']}m, {address['zip']}")


# start
dict_1()
