
import boto3
import csv
from decimal import Decimal

# Connect to DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-south-1'
)

# Function to upload CSV data
def upload_csv(filename, table_name, number_fields):

    table = dynamodb.Table(table_name)

    with open(filename, 'r', newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        with table.batch_writer() as batch:

            for row in reader:

                # Convert specified attributes to numbers
                for field in number_fields:
                    row[field] = Decimal(row[field])

                batch.put_item(Item=row)

    print(f"Successfully uploaded data to {table_name}")


# Upload player data
upload_csv(
    'Activity13_DynamoDB_players.csv',
    'players',
    ['level', 'coins']
)

# Upload session data
upload_csv(
    'Activity13_DynamoDB_sessions.csv',
    'sessions',
    ['login_time', 'expiry_time']
)

print("Both CSV files uploaded successfully!")
