import json

Myself = [   {
        "name":"Ariyan Islam hridoy",
        "Grade":[1,2,3],
        "Course":{
            "Data Science ":111,
            "Artificial Intelligence ": 111,
            "Operating System":111,
            "Software Engineering":111
        }
    },
    {
        "Semester":7,
        "University":"Daffodil International University"

    }
]

with open("demo.json" ,'w') as f :
    json.dump(Myself , f ,indent=4)
    
with open("demo.json", 'r') as f:
    data = json.load(f)
    print(data)    