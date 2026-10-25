from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import uuid
from datetime import datetime, timezone
from decimal import Decimal

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret"

# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")

# Replace with your actual DynamoDB table name
table = dynamodb.Table("Employees")


@app.route("/")
def index():
    # Retrieve employee records
    response = table.scan()
    employees = response.get("Items", [])

    # Continue scanning if DynamoDB returns more records
    while "LastEvaluatedKey" in response:
        response = table.scan(
            ExclusiveStartKey=response["LastEvaluatedKey"]
        )
        employees.extend(response.get("Items", []))

    return render_template("index.html", employees=employees)


@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    department = request.form.get("department", "").strip()
    skill = request.form.get("skill", "").strip()

    if not name or not email:
        flash("Employee name and email are required.", "error")
        return redirect(url_for("index"))

    employee_id = str(uuid.uuid4())

    # Save employee details in DynamoDB
    table.put_item(
        Item={
            "employee_id": employee_id,
            "name": name,
            "email": email,
            "department": department,
            "skill": skill,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        ConditionExpression="attribute_not_exists(employee_id)"
    )

    flash("Employee added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<employee_id>", methods=["POST"])
def delete_employee(employee_id):
    # Delete employee record from DynamoDB
    table.delete_item(
        Key={"employee_id": employee_id}
    )

    flash("Employee deleted successfully.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
