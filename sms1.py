import boto3


def lambda_handler(event, context):
    sms("Hi")

def sms(cart):
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id="AKIAJY34LQJ3YT5S274Q",
        aws_secret_access_key="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",
        region_name="us-east-1"
    )
    
    # Create the topic if it doesn't exist (this is idempotent)
    topic = client.create_topic(Name="notifications")
    topic_arn = topic['TopicArn']  # get its Amazon Resource Name
    
    # Add SMS Subscribers
    some_list_of_contacts = ["+15854347002","+15854138783"]
    for number in some_list_of_contacts:
        client.subscribe(
            TopicArn=topic_arn,
            Protocol='sms',
            Endpoint=number  # <-- number who'll receive an SMS message.
        )
    
    # Publish a message.
    client.publish(Message=cart, TopicArn=topic_arn)