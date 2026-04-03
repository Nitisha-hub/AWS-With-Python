# EC2 Automation Script using boto3
# Author: Nitisha Mali
# Description: Start, stop and check EC2 instance status

import boto3

# Create EC2 client   
ec2 = boto3.client('ec2')

INSTANCE_ID = 'your-instance-id'  # replace with your EC2 instance ID

def start_instance():
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("✅ EC2 instance started")

def stop_instance():
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("🛑 EC2 instance stopped")

def check_status():
    response = ec2.describe_instance_status(InstanceIds=[INSTANCE_ID])
    print("📊 Status:", response)

if __name__ == "__main__":
    print("1. Start Instance")
    print("2. Stop Instance")
    print("3. Check Status")

    choice = input("Enter choice: ")

    if choice == "1":
        start_instance()
    elif choice == "2":
        stop_instance()
    elif choice == "3":
        check_status()
    else:
        print("Invalid choice")
