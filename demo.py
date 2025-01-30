from us_visa.pipline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()

'''
import pymongo
import os
import certifi

MONGODB_URL = os.getenv("MONGODB_URL")  # Read from environment variable
print(MONGODB_URL)

if not MONGODB_URL:
    print("❌ Environment variable 'MONGODB_URL' is not set.")
else:
    try:
        client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=certifi.where())
        client.admin.command('ping')  # Simple test command
        print("✅ Connection to MongoDB successful!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
'''