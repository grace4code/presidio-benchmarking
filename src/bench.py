import json
from presidio_analyzer import AnalyzerEngine
from sklearn.metrics import precision_score, recall_score, f1_score

analyzer = AnalyzerEngine()


def benchmark(records, output_file="results.json"):
    results = {}
    for record in records:
        entity = record["entity_type"]
        text = record["text"]

        # Run Presidio
        analyzed = analyzer.analyze(text=text, language="en")

        # Build TP/FP/FN counts
        tp, fp, fn = 0, 0, 0
        detected_entities = [res.entity_type for res in analyzed]

        if entity in detected_entities:
            tp += 1
        else:
            fn += 1

        for det in detected_entities:
            if det != entity:
                fp += 1

        # Update entity-level results
        if entity not in results:
            results[entity] = {
                "true_positives": 0,
                "false_positives": 0,
                "false_negatives": 0,
                "support": 0
            }

        results[entity]["true_positives"] += tp
        results[entity]["false_positives"] += fp
        results[entity]["false_negatives"] += fn
        results[entity]["support"] += 1

    # Compute Precision, Recall, F1
    for entity, stats in results.items():
        tp = stats["true_positives"]
        fp = stats["false_positives"]
        fn = stats["false_negatives"]

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / \
            (precision + recall) if (precision + recall) > 0 else 0.0

        stats["precision"] = round(precision, 2)
        stats["recall"] = round(recall, 2)
        stats["f1_score"] = round(f1, 2)

    # Save JSON
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    return results
