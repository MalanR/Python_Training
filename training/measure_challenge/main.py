
from process_api import ProcessAPI
from measures_module import Measures
from triggers_module import Triggers
import uuid

data_structure = {
    "measurement": [
        {
            "code": uuid.uuid4(),
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
            "code": uuid.uuid4(),
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

api = ProcessAPI()
api.add_module("measure", Measures)
api.add_module("triggers", Triggers)
api.call("measure", "create", {"api": api, "data_structure": data_structure})
print(data_structure)
