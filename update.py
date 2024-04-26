import time
import random
from pymongo import MongoClient
from faker import Faker


# Initialize Faker for document generation
fake = Faker()

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client.seng533
collection = db['seng533']

# Generate data 
def generate_fake_data(collection, num_records):
    fake = Faker()
    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'id': random.randrange(1001,10000),
            'bool': bool(random.getrandbits(1)),
        }
        collection.insert_one(record)

        

# Number of documents to update 
num_docs_to_update = [1, 5, 10, 100, 1000, 10000, 100000]

# Update types 
update_fields = ['name', 'id', 'bool']

update_to_do = {
    'name': 'update test',
    'id': 111,
    'bool': False,
}

update_results = []


for num_docs in num_docs_to_update:
    for field in update_fields:
        # Generate documents
        documents = [generate_fake_data(collection, num_docs)]

        # Time the update 
        start_time = time.time_ns()

        # update documents
        collection.update_many({}, { "$set": {field: update_to_do[field]}})

        end_time = time.time_ns()

        # Calculate and store results
        elapsed_time = end_time - start_time
        update_results.append({
            "num_docs": num_docs,
            "field_type": str(type(update_to_do[field])),
            "elapsed_time_seconds": elapsed_time,
            "updates_per_second": elapsed_time / num_docs,
            "start_time": start_time,
            "end_time": end_time,
        })

        # print(f"Number of Updates: {num_docs}, Type of Field updated: {type(update_to_do[field])}, "
        #   f"Start Time: {start_time:.2f}, End Time: {end_time:.2f}, "
        #   f"Elapsed Time: {(elapsed_time):.2f}")
        
        collection.drop()

# Print results
for result in update_results:
    print(f"Number of Documents: {result['num_docs']}, Type of Field updated: {result['field_type']}, "
          f"Elapsed Time (seconds): {result['elapsed_time_seconds']:.2f}, "
          f"Updates per Second: {result['updates_per_second']:.2f}")

# Clean up: Comment out the next line if you want to keep the data in the database
collection.drop()