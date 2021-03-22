#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import Instance, AwsProvider


class MyStack(TerraformStack):
  def __init__(self, scope: Construct, ns: str):
    super().__init__(scope, ns)

    AwsProvider(self, 'Aws', region='us-west-1')
    helloInstance = Instance(self, 'hello',
      ami="ami-031b673f443c2172c",
      instance_type="t2.micro",
    )

    TerraformOutput(self, 'hello_public_ip',
      value=helloInstance.public_ip
    )

app = App()
stack = MyStack(app, "ec2-instance")

stack.add_override('terraform.backend', {
  'remote': {
    'hostname': 'app.terraform.io',
    'organization': 'omegazyadav',
    'workspaces': {
      'name': 'python'
    }
  }
})

app.synth()
