import time
from pymongo import MongoClient
from faker import Faker

# MongoDB connection parameters
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DB_NAME = 'seng533'
COLLECTION_NAME = 'seng533'

# Function to connect to MongoDB


def connect_to_mongodb():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

# Function to generate fake data


def generate_fake_data(collection, num_records):
    fake = Faker()
    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone': fake.phone_number()
        }
        collection.insert_one(record)

# Function to perform read operations benchmarking


def benchmark_read_operations(collection):
    # Simple find operation
    start_time = time.time()
    simple_find_result = collection.find_one()
    end_time = time.time()
    simple_find_time = end_time - start_time
    print("Simple Find Time:", simple_find_time)

    # Complex query
    start_time = time.time()
    complex_query_result = collection.find({"field": {"$gt": 10, "$lt": 20}})
    end_time = time.time()
    complex_query_time = end_time - start_time
    print("Complex Query Time:", complex_query_time)

    # Range search
    start_time = time.time()
    range_search_result = collection.find({"field": {"$gte": 5, "$lte": 15}})
    end_time = time.time()
    range_search_time = end_time - start_time
    print("Range Search Time:", range_search_time)

    # Measure throughput
    num_operations = 1000
    start_time = time.time()
    for i in range(num_operations):
        collection.find_one()
    end_time = time.time()
    throughput = num_operations / (end_time - start_time)
    print("Throughput:", throughput, "ops/sec")

    # Index usage efficiency
    index_usage = collection.index_information()
    print("Index Usage Efficiency:", index_usage)


if __name__ == "__main__":
    collection = connect_to_mongodb()

    # Generate fake data
    num_records = 1000
    generate_fake_data(collection, num_records)

    # Benchmark read operations
    benchmark_read_operations(collection)
