import json
import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client("ec2")
    
    # Get all EC2 instances
    instances = ec2_client.describe_instances()
    
    non_compliant_instances = []
    
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            for interface in instance.get("NetworkInterfaces", []):
                if "Association" in interface and "PublicIp" in interface["Association"]:
                    non_compliant_instances.append(instance_id)
    
    if non_compliant_instances:
        return {
            "compliance_type": "NON_COMPLIANT",
            "annotation": f"Instances with public IPs: {', '.join(non_compliant_instances)}"
        }
    else:
        return {
            "compliance_type": "COMPLIANT",
            "annotation": "No instances with public IPs found."
        }
