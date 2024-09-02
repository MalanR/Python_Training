
class Triggers:
    @staticmethod
    def  create(triggers, measure_code):
        for trigger in triggers:
            trigger["measure_code"] = measure_code


