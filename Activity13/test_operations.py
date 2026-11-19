
import boto3
import time

# Connect to DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-south-1'
)

players = dynamodb.Table('players')

player_id = 'TEST-PLAYER-001'

# 1. INSERT operation
print("\n1. INSERT operation")

players.put_item(
    Item={
        'player_id': player_id,
        'name': 'TestGamer',
        'level': 10,
        'coins': 500,
        'country': 'IN'
    }
)

print("Player inserted successfully!")

time.sleep(3)

# 2. MODIFY operation
print("\n2. MODIFY operation")

players.update_item(
    Key={
        'player_id': player_id
    },
    UpdateExpression='SET #lvl = :level, coins = :coins',
    ExpressionAttributeNames={
        '#lvl': 'level'
    },
    ExpressionAttributeValues={
        ':level': 25,
        ':coins': 1500
    }
)

print("Player updated successfully!")

time.sleep(3)

# 3. REMOVE operation
print("\n3. REMOVE operation")

players.delete_item(
    Key={
        'player_id': player_id
    }
)

print("Player deleted successfully!")

print("\nAll three operations completed!")
