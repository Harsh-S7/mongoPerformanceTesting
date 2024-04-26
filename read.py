from pymongo import MongoClient
import time
from faker import Faker

# Initialize Faker for document generation
fake = Faker()

# Function to generate a single document with diverse fields


def generate_document():
    return {
        "name": fake.name(),  # String field
        "age": fake.random_int(min=18, max=100),  # Integer field
        "is_active": fake.boolean(),  # Boolean field
        "email": fake.email(),
        "address": fake.address(),
        "profile": {
            "birthdate": fake.date_of_birth().isoformat(),
            "bio": fake.text(max_nb_chars=200)
        }
    }


# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client.seng533
collection = db['performance_test']

# Number of documents to query for each test
num_docs_per_test = [1, 5, 10, 100, 1000, 10000, 100000]

# Insert a fixed large number of documents (e.g., 100,000) to test the queries against
large_doc_count = 100000
documents = [generate_document() for _ in range(large_doc_count)]
collection.insert_many(documents)

# Function to test read performance


def test_read_performance(field, num_docs):
    query = {}
    if field == "name":  # Example for string
        query = {"name": documents[0]['name']}
    elif field == "age":  # Example for integer
        query = {"age": documents[0]['age']}
    elif field == "is_active":  # Example for boolean
        query = {"is_active": documents[0]['is_active']}

    start_time = time.time_ns()
    cursor = collection.find(query).limit(num_docs)
    results = list(cursor)  # Force the cursor to retrieve data
    end_time = time.time_ns()

    elapsed_time = end_time - start_time
    inverse_throughput = float(elapsed_time / num_docs)

    print(f"Field: {field}, Number of Documents: {num_docs}, "
          f"Elapsed Time (ns): {elapsed_time}, 1/Throughput (ns/document): {inverse_throughput}")


# Test reads for different field types and numbers of documents
fields = ['name', 'age', 'is_active']
for field in fields:
    for count in num_docs_per_test:
        test_read_performance(field, count)

# Clean up: Uncomment the next line if you want to clear the test data
collection.drop()
