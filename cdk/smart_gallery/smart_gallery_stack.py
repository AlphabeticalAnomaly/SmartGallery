from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamo,
    aws_iam as iam,
)


class SmartGalleryStack(Stack):
    # noinspection PyTypeChecker
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        gallery_lambda = lambda_.Function(self, "GalleryLambda",
                                          handler='lambda_function.lambda_handler',
                                          runtime=lambda_.Runtime.PYTHON_3_8,
                                          code=lambda_.Code.from_asset(path="../lambda_code/src"),
                                          layers=[lambda_.LayerVersion(self, "MyLayer",
                                                                       code=lambda_.Code.from_asset(
                                                                           path="../lambda_code/layers/layer.zip"))
                                                  ],
                                          )

        bucket = s3.Bucket(self, "GalleryBucket", bucket_name="gallerybucket1241210")
        bucket.grant_read_write(gallery_lambda)
        bucket.grant_public_access()

        table = dynamo.TableV2(self, "Table", partition_key=dynamo.Attribute(name="image",
                                                                             type=dynamo.AttributeType.STRING),
                               sort_key=dynamo.Attribute(name="description",
                                                         type=dynamo.AttributeType.STRING),
                               contributor_insights=True,
                               table_class=dynamo.TableClass.STANDARD_INFREQUENT_ACCESS,
                               point_in_time_recovery=True,
                               table_name="GalleryTable",
                               )
        gallery_lambda.add_to_role_policy(iam.PolicyStatement(effect=iam.Effect.ALLOW,
                                                              resources=[table.table_arn],
                                                              actions=["dynamodb:BatchGetItem",
                                                                       "dynamodb:BatchWriteItem",
                                                                       "dynamodb:DeleteItem",
                                                                       "dynamodb:GetItem",
                                                                       "dynamodb:PutItem",
                                                                       "dynamodb:Query",
                                                                       "dynamodb:UpdateItem"
                                                                       ]
                                                              ))
        api = apigateway.LambdaRestApi(self, "GalleryApi", rest_api_name="GalleryRestApi", handler=gallery_lambda,
                                       proxy=False)

        root_resource = api.root
        root_resource.add_method("POST")
