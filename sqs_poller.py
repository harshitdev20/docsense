import boto3
import subprocess

sqs = boto3.client("sqs", region_name="us-east-1")
QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/759802535511/Docsense_queue"

def poll():
    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )
        messages = response.get("Messages", [])
        for msg in messages:
            print("New data event received, rebuilding embeddings...")
            subprocess.run(["python", "scripts/build_embeddings.py"])
            sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=msg["ReceiptHandle"])

if __name__ == "__main__":
    poll()