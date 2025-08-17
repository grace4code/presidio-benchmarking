import json
from datetime import datetime


class ResultsSaver:
    def __init__(self, output_file="results.json"):
        self.output_file = output_file

    def save(self, results):
        data = {
            "timestamp": datetime.now().isoformat(),
            "results": results
        }
        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)
