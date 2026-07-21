import argparse
import time

parser = argparse.ArgumentParser(description="Warmup test job")
args = parser.parse_args()

print("Warmup job started", flush=True)

for i in range(10):
    print(f"Running step {i + 1}/10", flush=True)
    time.sleep(5)

print("Warmup job completed", flush=True)
