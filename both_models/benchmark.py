from presidio_analyzer import AnalyzerEngine


def benchmark(records):
    analyzer = AnalyzerEngine()
    results = []

    total_tp, total_fp, total_fn, total_exact = 0, 0, 0, 0
    total_expected, total_detected = 0, 0

    for rec in records:
        text = rec["text"]
        expected_entities = rec["entities"]

        # Run Presidio analyzer
        presidio_results = analyzer.analyze(text=text, language="en")

        # Convert to comparable dicts
        expected = [
            (e["entity_type"], e["start"], e["end"], e["text"])
            for e in expected_entities
        ]
        detected = [
            (r.entity_type, r.start, r.end, text[r.start:r.end])
            for r in presidio_results
        ]

        matched = []
        exact_match = 0

        # True positives: entity type + overlapping span
        for d in detected:
            for e in expected:
                if d[0] == e[0]:  # same entity type
                    # check span overlap
                    if not (d[2] <= e[1] or d[1] >= e[2]):
                        matched.append(d)
                        # exact index match
                        if d[1] == e[1] and d[2] == e[2]:
                            exact_match += 1
                        break

        tp = len(matched)
        fp = len(detected) - tp
        fn = len(expected) - tp

        total_tp += tp
        total_fp += fp
        total_fn += fn
        total_exact += exact_match
        total_expected += len(expected)
        total_detected += len(detected)

        results.append({
            "input_text": text,
            "expected": expected_entities,
            "detected": [
                {"entity_type": r.entity_type, "start": r.start,
                    "end": r.end, "text": text[r.start:r.end]}
                for r in presidio_results
            ],
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "exact_match": exact_match
        })

    # Global metrics
    precision = total_tp / total_detected if total_detected else 0
    recall = total_tp / total_expected if total_expected else 0
    f1 = (2 * precision * recall) / \
        (precision + recall) if (precision+recall) else 0
    exact_accuracy = total_exact / total_expected if total_expected else 0

    metrics = {
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1_score": round(f1, 3),
        "exact_index_accuracy": round(exact_accuracy, 3),
        "total_expected": total_expected,
        "total_detected": total_detected,
        "total_tp": total_tp,
        "total_fp": total_fp,
        "total_fn": total_fn
    }

    return results, metrics
