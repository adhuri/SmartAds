import boto3
import time


LOCATION_QUEUE_NAME='hacknc_location'
#IMAGES_QUEUE_NAME='hacknc_images'

# Get the service resource
sqs = boto3.resource('sqs',region_name='us-west-2',aws_access_key_id='AKIAIM2MJLQFQWJJKRXA',aws_secret_access_key='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')



def create_queues():
    # Already Created!! Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(QueueName=LOCATION_QUEUE_NAME, Attributes={'DelaySeconds': '5'})
    #queue = sqs.create_queue(QueueName=IMAGES_QUEUE_NAME, Attributes={'DelaySeconds': '5'})


def get_batch_location_msgs(queue):
    batch_msgs=[]
    for i in range(5):
        # Process messages by printing out body and optional author name
        msg={}
        for message in queue.receive_messages():
            # Get the custom author message attribute if it was set
            username = ''
            if message.message_attributes is not None:
                username = message.message_attributes.get('username').get('StringValue')
                lat=message.message_attributes.get('lat').get('StringValue')
                longi=message.message_attributes.get('longi').get('StringValue')
                if username:
                    username = ' ({0})'.format(author_name)
                    msg.update({'username':username})
                if lat:
                    lat=float(lat)
                    msg.update({'lat':lat})
                if longi:
                    longi=float(longi)
                    msg.update({'longi':longi})

            batch_msgs.append(msg)

    # Print out the body and author (if set)
    print batch_msgs

    # Let the queue know that the message is processed
    #message.delete()

    return batch_msgs

#Test method to push messages, but this should be done from Android App
def push_messages(queue):
    queue.send_message(MessageBody='boto3', MessageAttributes={
                'username': {
                    'StringValue': 'chethan',
                    'DataType': 'String'
                    },
                'lat': {
                    'StringValue': '20',
                    'DataType': 'String'
                    },
                'longi':{
                    'StringValue': '30',
                    'DataType': 'String'
                    }
                })


def main():
    try:
        location_queue = sqs.get_queue_by_name(QueueName=LOCATION_QUEUE_NAME)
    except Exception as e:
        print 'Exception occured while retrieving location queue'+ e
    #try:
    #    images_queue=sqs.get_queue_by_name(QueueName=IMAGES_QUEUE_NAME)
    #except Exception as e:
    #    print 'Exception occured while retrieving images queue'+ e
    push_messages(location_queue)
    push_messages(location_queue)
    push_messages(location_queue)
    push_messages(location_queue)
    push_messages(location_queue)

    while(1):
        time.sleep(5)
        #Fetch five messages from the Queue
        print "cool"
        batch_location_msgs=get_batch_location_msgs(location_queue)
        print batch_location_msgs

main()
