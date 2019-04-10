import json

people_string = """
{
    "people":[
        {
            "name": "Narendra Maurya",
            "age": 25,
            "phone_number": "(+91)6360535414",
            "languages":[
                "Python",
                "Javascript",
                "PHP",
                "Swift",
                "Dart"
            ],
            "frontend_frameworks":[
                "Angular",
                "Ionic",
                "Flutter SDK",
                "React",
                "Vue.js"
            ],
            "backend_frameworks":[
                "Laravel",
                "Node.js",
                "Dajngo",
                "Flask",
                "Slim PHP"
            ]
        },
        {
            "name": "Jhon Doe",
            "age": 32,
            "phone_number": "(+01)7275790917",
            "languages":[
                "Python",
                "Java",
                "Javascript",
                "Swift"
            ],
            "frontend_frameworks":[
                "Angular",
                "React",
                "Vue.js"
            ],
            "backend_frameworks":[
                "Dajngo",
                "Flask",
                "Node.js"
            ]
        }
    ]
}
"""


data = json.loads(people_string)

# print(type(data))
# print(data['people'])

for person in data['people']:
    # print(person['name'], person['age'])
    del person['phone_number']
    # print(person)

new_json = json.dumps(data)
new_json = json.dumps(data, indent=2, sort_keys=True)

print(new_json)
