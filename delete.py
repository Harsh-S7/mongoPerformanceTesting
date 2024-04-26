import time
from pymongo import MongoClient
from faker import Faker

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']  # Replace 'test_database' with your database name
# Replace 'test_collection' with your collection name
collection = db['test_collection']

# Initialize Faker
fake = Faker()

# Function to generate fake document with given size


def generate_document(doc_size):
    document = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "profile": {
            "birthdate": fake.date_of_birth().isoformat(),
            "bio": fake.text(max_nb_chars=200)
        }
    }

    # Add additional data to increase document size
    if doc_size > 1:
        document["extended_info"] = {"activities": [
            fake.text(max_nb_chars=200) for _ in range(doc_size)]}

    return document

# Function to insert fake data with varying sizes


def insert_delete_fake_data(doc_sizes, num_docs_per_size):
    for size in doc_sizes:
        for num_docs in num_docs_per_size:
            documents = [generate_document(size) for _ in range(num_docs)]
            collection.insert_many(documents)
            start_time = time.time_ns()
            collection.delete_many({})
            end_time = time.time_ns()
            elapsed_time = float(end_time - start_time)
            delete_time_for_one_document = float(elapsed_time / num_docs)
            print(f"Document Size: {size}, Number of Documents: {num_docs}, "
                  f"Elapsed Time (nanoseconds): {elapsed_time:.2f}, "
                  f"1/Throughput: {delete_time_for_one_document:.2f}")


# Define document sizes
document_sizes = [1, 5, 10]

# Define number of documents per size to delete
num_docs_per_size = [1, 5, 10, 100, 1000, 10000, 100000, 1000000]

# Insert fake data with varying sizes and amounts
insert_delete_fake_data(document_sizes, num_docs_per_size)

# Close MongoDB connection
client.close()
