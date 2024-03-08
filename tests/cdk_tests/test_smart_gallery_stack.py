import aws_cdk as core
import aws_cdk.assertions as assertions
from smart_gallery.smart_gallery_stack import SmartGalleryStack


def test_synthesizes_properly():
    app = core.App()
    stack = SmartGalleryStack(app, "SmartGallery")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "lambda_function.lambda_handler",
            "Runtime": "python3.8"
        },
    )

    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketName": "gallerybucket1241210"
        }
    )

    template.has_resource_properties(
        "AWS::DynamoDB::GlobalTable",
        {
            "TableName": "GalleryTable",
            "AttributeDefinition": {
                {
                    "AttributeName": "image",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "description",
                    "AttributeType": "S"
                }
                },
            "BillingMode": "PAY_PER_REQUEST"

        }
    )

    template.has_resource_properties(
        "AWS::ApiGateway::RestApi",
        {
            "Name": "GalleryRestApi"
        }
    )
