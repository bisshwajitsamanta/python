import boto3
import datetime

# Initialize the CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Define your custom metric dimensions (if needed)
dimensions = [
    {
        'Name': 'SemaphoreCDBuild',
        'Value': 'Succeeded'
    }
]

# Define the metric name and namespace
metric_name = 'deploy_job'
namespace = 'MDR'

# Create a timestamp for the data point (UTC)
timestamp = datetime.datetime.utcnow()

# Define the value of your custom metric
metric_value = 1

# Publish the custom metric to CloudWatch
response = cloudwatch.put_metric_data(
    Namespace=namespace,
    MetricData=[
        {
            'MetricName': metric_name,
            'Dimensions': dimensions,
            'Timestamp': timestamp,
            'Value': metric_value,
            'Unit': 'Count'  # Specify the appropriate unit for your metric
        }
    ]
)

print(f"Published custom metric to CloudWatch: {response}")
