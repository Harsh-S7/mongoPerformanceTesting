from pymongo import MongoClient
import time
import random
from faker import Faker

# Initialize Faker for document generation
fake = Faker()

# Function to generate a single document


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


# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client.seng533
collection = db['seng533']

# Define different document sizes to test
# Number of activities to add. Adjust based on your needs.
documents_sizes = [1, 5, 10]

# Number of documents to insert for each size
num_docs_per_size = [1, 5, 10, 100, 1000, 10000, 100000, 1000000]

insertion_results = []

for size in documents_sizes:
    for count in num_docs_per_size:
        # Generate documents
        documents = [generate_document(size) for _ in range(count)]
        # Measure insertion time
        start_time = time.time_ns()
        st1 = time.time()
        collection.insert_many(documents)
        st2 = time.time()
        end_time = time.time_ns()

        # Calculate and store results
        elapsed_time = end_time - start_time
        insertion_results.append({
            "document_size": size,
            "num_documents": count,
            "elapsed_time_seconds": elapsed_time,
            "documents_per_second": count / (st2-st1)
        })

# Print results
for result in insertion_results:
    print(f"Document Size: {result['document_size']}, Number of Documents: {result['num_documents']}, "
          f"Elapsed Time (seconds): {result['elapsed_time_seconds']:.2f}, "
          f"Documents per Second: {result['documents_per_second']:.2f}")

# Clean up: Comment out the next line if you want to keep the data in the database
collection.drop()
