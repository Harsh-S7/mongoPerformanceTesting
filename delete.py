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


def insert_fake_data(doc_sizes, num_docs_per_size):
    for size in doc_sizes:
        for num_docs in num_docs_per_size:
            start_time = time.time()
            for _ in range(num_docs):
                fake_document = generate_document(size)
                collection.insert_one(fake_document)
            end_time = time.time()
            elapsed_time = end_time - start_time
            documents_per_second = num_docs / elapsed_time

            print(f"Document Size: {size}, Number of Documents: {num_docs}, "
                  f"Elapsed Time (seconds): {elapsed_time:.2f}, "
                  f"Documents per Second: {documents_per_second:.2f}")

            # Perform delete operation after each insertion
            delete_test()

# Function to perform delete operation


def delete_test():
    start_time = time.time()
    # Perform delete operation here
    # Example: collection.delete_many({}) to delete all documents
    collection.delete_many({})
    end_time = time.time()
    print(f"Delete operation executed in {end_time - start_time:.2f} seconds")


# Define document sizes
document_sizes = [1, 5, 10]

# Define number of documents per size to delete
num_docs_per_size = [1, 5, 10, 100, 1000, 10000, 100000, 1000000]

# Insert fake data with varying sizes and amounts
insert_fake_data(document_sizes, num_docs_per_size)

# Close MongoDB connection
client.close()
