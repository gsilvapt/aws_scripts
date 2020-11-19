# EC2 Instances  

## Helper Scripts  
Procedural scripting is not ideal. CF provides Python based helper scripts to optimise this. It comes preinstalled on
Amazon Linux AMI. When we need to execute them, we need to specifically call them.

Reference can be found here: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html


There are 4 helpers scripts provided by AWS:
- `cfn-init`: Reads and interprets Metadata to execute AWS::CloudFormation::Init
- `cfn-signal`: Used to signal when resource or application is ready
- `cfn-get-metadata`: Used to retrieve metadata based on a specific key
- `cfn-hup`: Used to check for updates to metadata and execute custom hooks
