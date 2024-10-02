from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct


class AppStack(Stack):

    @property
    def lambda_code_data(self):
        return self.lambda_code

    @property
    def lambda_layer_code_data(self):
        return self.lambda_layer_code

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_code = _lambda.Code.from_cfn_parameters()
        lambda_layer_code = _lambda.Code.from_cfn_parameters()

        app_function = _lambda.Function(
            self, 'AppCoinDeskFunction',
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=lambda_code,
            handler='app.handler',
            environment={
                "API_URL": "https://api.coindesk.com/v1/bpi/currentprice.json"
            }
        )

        app_layer = _lambda.LayerVersion(
            self, 'AppCoinDeskLayer',
            code=lambda_layer_code,
            layer_version_name="RequestHTTPLayer",
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_10],
            description='Capa para usar la librería de requests y hacer peticiones HTTP'
            )

        app_function.add_layers(app_layer)
        app_version = app_function.current_version

        app_alias_dev = _lambda.Alias(
            self, 'AppCoinDeskAlias',
            alias_name='AppCoinDesk_Dev',
            version=app_version
        )

        self.alias = app_alias_dev
        self.lambda_code = lambda_code
        self.lambda_layer_code = lambda_layer_code

        apigw.LambdaRestApi(
            self, 'AppCoinDeskEndpoint',
            handler=app_function,
        )
