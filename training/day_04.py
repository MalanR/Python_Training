# objective:
#     create a process api. (in its own file)
#     register a module called measure and register a module called triggers.
#     your measures module should handle the creation of measures. (this should be a module that also lives in its own file)
#     your triggers module should handle the creation of triggers. (this should be a module that also lives in its own file)
#     we then want to append a new key value pair into the triggers dictionary that looks like this {"measure_code": measure_code.}
#     we then want to print out the result and verify that each trigger has this key value pair and that the code is equal to the measure code.
#     expected json result:
# data_structure = {
#     "measurement": [
#         {
#             "code": uuid(oyfd9s8sdfjdf-sdfh7),
#             "description": "Temperature",
#             "triggers": [
#                 {
#                     "code": "T1",
#                     "description": "Temperature is too high",
#                     "measure_code": "oyfd9s8sdfjdf-sdfh7"
#                 },
#                 {
#                     "code": "T2",
#                     "description": "Temperature is too low",
#                     "measure_code": "oyfd9s8sdfjdf-sdfh7"
#                 }
#             ]
#         }
# }
#     keep separation of concern in mind.
#    You will need to have a method in measuresModule that allows you to loop through the data structure
#     You then want to grab the get the desired code, and assign it to the triggers.
#     In your triggersModule you will also need a create measure that will loop through the triggers and assign the measure code to each trigger.
#    in your main.py file you want to be able to use the process api to call the modules and measures needed to perform the task.
#   Use the Measure_Challenge folder to store all you files.




data_structure = {
    "measurement": [
        {
            "code": uuid.uuid4,
            "description": "Temperature",
            "triggers": [
                {
                    "code": "T1",
                    "description": "Temperature is too high",
                },
                {
                    "code": "T2",
                    "description": "Temperature is too low",
                }
            ]
        },
        {
            "code": uuid.uuid4,
            "description": "Humidity",
            "triggers": [
                {
                    "code": "H1",
                    "description": "Humidity is too high",
                },
                {
                    "code": "H2",
                    "description": "Humidity is too low",
                },
                {
                    "code": "H3",
                    "description": "Humidity is normal",
                }
            ]
        }
    ]
}
