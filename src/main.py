from data_generator import generate_fake_records
from bench import benchmark


def main():
    print("🔹 Generating fake data...")
    records = generate_fake_records(num_records=20)

    print("🔹 Running benchmark...")
    results = benchmark(records, "results.json")

    print("✅ Benchmark complete. Results saved in results.json")


if __name__ == "__main__":
    main()
