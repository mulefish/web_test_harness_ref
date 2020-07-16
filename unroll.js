
let stack = [] 
function unrollJson(the_path, item ) {
    if ( item instanceof Object ) {
        // a collection 
        for ( let key in item ) {
            if ( item.hasOwnProperty( key )) {
                unrollJson ( the_path + key + " -> ", item[key])
            }
        }
    } else {
        // primitive
        stack.push(the_path + ": " + item)
    }
}
////////// Mini-self test
if (require.main === module) {
    // if __name__ == ...
    const data = {
        "a":"ichi",
        "b":"ni",
        "LoL":[ // list of lists
            "x","y","z"
        ],
        "HoL": { // hash of lists 
            "o":[0,1],
            "p":[2,3]
        },
        "HoH": {  // hash of hashes
            "dog":{"bark":true, "meow":false}
        }, 
        "HoHoH": { // hash of hashes of hashes
            "first":{"second":{"third":"The payload!"}}
        }
    }

    unrollJson("", data)
    stack = stack.sort()

    const expect  = "HoHoH -> first -> second -> third -> : The payload!"
    isOk = false 
    stack.forEach((item,i)=>{
        if ( expect == item ) {
            isOk = true 
        }
        console.log( i , item )
    })

    if ( isOk ) {
        console.log("PASS - it works")    
    } else {
        console.log("FAIL - try again ")
    }
}