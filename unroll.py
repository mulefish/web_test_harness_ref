
def unroll_json( the_path, obj, the_stack):
    if isinstance(obj, dict):
        for key in obj:
            unroll_json( the_path + key + " -> ", obj[key], the_stack)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            unroll_json( the_path + "{} -> ".format(i), obj[i], the_stack)
    else:
        x = "{} |{}|".format(the_path, obj)
        # print(x)
        the_stack.append(x) # < ----  OMG! Why does not the_stack get the var 'x'?!

    return the_stack


def doit():
    data = {
        "a":"ichi",
        "b":"ni",
        "LoL":[ # // list of lists
            "x","y","z"
        ],
        "HoL": { # // hash of lists 
            "o":[0,1],
            "p":[2,3]
        },
        "HoH": {  # // hash of hashes
            "dog":{"bark":True, "meow":False}
        }, 
        "HoHoH": { # // hash of hashes of hashes
            "first":{"second":{"third":"The payload!"}}
        }
    }
    the_stack = unroll_json("", data, [])
    expected = "HoHoH -> first -> second -> third ->  |The payload!|"

    try: 
        if expected in the_stack:
            print("PASS it worked ")
        else:
            print("FAIL it failed")
    except Exception as boom:
        print( the_stack ) # < ------------- Why is the_stack 'None'?!
        print("boom! {} ".format(boom))

if __name__ == "__main__":
    doit()
