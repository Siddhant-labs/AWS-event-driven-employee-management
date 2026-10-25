import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    for record in event.get("Records", []):
        event_name = record.get("eventName", "UNKNOWN")

        print(f"Event type: {event_name}")

        if event_name == "INSERT":
            employee = record.get("dynamodb", {}).get(
                "NewImage", {}
            )
            print("New employee added:")
            print(json.dumps(employee))

        elif event_name == "MODIFY":
            employee = record.get("dynamodb", {}).get(
                "NewImage", {}
            )
            print("Employee record updated:")
            print(json.dumps(employee))

        elif event_name == "REMOVE":
            employee = record.get("dynamodb", {}).get(
                "OldImage", {}
            )
            print("Employee record removed:")
            print(json.dumps(employee))

        else:
            print(f"Unhandled event: {event_name}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "DynamoDB events processed",
            "processed_records": len(event.get("Records", [])),
            "processed_at": datetime.now(timezone.utc).isoformat()
        })
    }
