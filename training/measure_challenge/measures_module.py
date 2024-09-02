
class Measures:
    @staticmethod
    def create(api, data_structure):
        measurements = data_structure.get("measurement", [])
        for measure in measurements:
            measure_code = measure.get("code")
            triggers = measure.get("triggers", [])

            if api is not None:
                api.call("triggers", "create", {"measure_code": measure_code, "triggers": triggers})
            else:
                print("api is None")
#
# def create_triggers(api, triggers, measure_code):
#     for trigger in triggers:
#         trigger["measure_code"] = measure_code
#     api.call("triggers", "create", {"measure_code": measure_code, "triggers": triggers })



# obj = [1, 2, 3, 4, 5]
#
# for i in obj:
#     print(i)