from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, Instance

class MyEc2Stack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="us-east-1")

        Instance(self, "MyWebsiteInstance",
                 ami="ami-08d70e59c07c61a3a",  # Replace with a valid AMI for your region
                 instance_type="t2.micro",
                 tags={"Name": "MyWebsiteInstance"})

app = App()
MyEc2Stack(app, "my-ec2-website")

app.synth()
