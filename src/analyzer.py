from presidio_analyzer import AnalyzerEngine


class PresidioAnalyzer:
    def __init__(self):
        self.analyzer = AnalyzerEngine()

    def analyze(self, sentence, entities):
        results = self.analyzer.analyze(
            text=sentence,
            entities=entities,
            language="en"
        )
        return [(r.entity_type, r.start, r.end) for r in results]
