from pymongo import MongoClient
import time

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client.seng533
collection = db['seng533_read_test']

# Preload data to read
documents = [{"number": i} for i in range(1000000)]
collection.insert_many(documents)

# Number of documents to read in each test
read_counts = [1, 10, 100, 1000, 10000, 100000, 1000000]

read_results = []

for count in read_counts:
    start_time = time.time()
    documents = list(collection.find().limit(count))
    end_time = time.time()

    elapsed_time = end_time - start_time
    read_results.append({
        "num_documents": count,
        "elapsed_time_seconds": elapsed_time,
        "documents_per_second": count / elapsed_time
    })

# Print results
for result in read_results:
    print(f"Number of Documents: {result['num_documents']}, "
          f"Elapsed Time (seconds): {result['elapsed_time_seconds']:.2f}, "
          f"Documents per Second: {result['documents_per_second']:.2f}")

# Clean up
collection.drop()

"""

Number of Documents: 1, Elapsed Time (seconds): 0.08, Documents per Second: 12.82
Number of Documents: 10, Elapsed Time (seconds): 0.00, Documents per Second: 11096.04
Number of Documents: 100, Elapsed Time (seconds): 0.00, Documents per Second: 231601.55
Number of Documents: 1000, Elapsed Time (seconds): 0.00, Documents per Second: 217671.08
Number of Documents: 10000, Elapsed Time (seconds): 0.01, Documents per Second: 729279.29
Number of Documents: 100000, Elapsed Time (seconds): 0.08, Documents per Second: 1244582.13
Number of Documents: 1000000, Elapsed Time (seconds): 1.54, Documents per Second: 647879.92

"""
