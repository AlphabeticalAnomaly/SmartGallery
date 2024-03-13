from flask import Flask, request, jsonify
import awsgi
import boto3


SUPPORTED_FORMAT = ["image/png", "image/jpg", "image/jpeg", "image/jpe", "image/jfif",  "image/bpm",  "image/tiff"]

app = Flask("SmartGalleryStack")


@app.route('/', methods=["POST"])
def place_item():
    file = request.files["Image"]
    if file.content_type not in SUPPORTED_FORMAT:
        return jsonify(status=400, message="Unsupported file format.")
    else:
        s3 = boto3.resource("s3")
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table("GalleryTable")
        table.put_item(Item={"image": "Test", "description": "Test", "content": file.filename})
        s3.Bucket("gallerybucket1241210").put_object(Key=file.filename, Body=file)
        return jsonify(status=200, message="Done!")


def lambda_handler(event, context):
    try:
        return awsgi.response(app, event, context)
    except Exception as e:
        return jsonify(status=500, message="The server encountered an error.")



