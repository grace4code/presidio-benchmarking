import json
from generator import generate_dataset
from benchmark import benchmark

if __name__ == "__main__":
    # Generate synthetic dataset
    records = generate_dataset(300)  # increase dataset size for metrics

    # Run benchmark
    results, metrics = benchmark(records)

    # Save detailed results
    with open("benchmark_spacy_detailed.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    # Save metrics
    with open("benchmark_spacy_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4, ensure_ascii=False)

    print("✅ Benchmark completed.")
    print("📊 Metrics:", metrics)
    print("Results saved to benchmark_spacy_detailed.json and benchmark_spacy_metrics.json")
