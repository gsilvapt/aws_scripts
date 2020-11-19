# CF Features  

## Intrinsic Functions  
Built-in functions that help manage stacks.

## Multiple Resources  
We can reference other resources that exist using the intrinsic function `!Ref`.

## Pseudo Parameters  
These are similar to env vars and can be referenced using `!Ref` intrinsic function. We can expect these to exist.
A full list can be seen at https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html

## Mappings  
Mappings enables users to use an input value to determine another value. For example, how can we determine the AMI ID 
based on the region? Through mappings.
These are triggered using `!FindInMap` function. => `!FindInMap [ mapName, TopLvlKey, SecondLvlKey ]`

Guide and recommendation: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html

## Input Parameters  
Enable input custom values to the template. They are defined within the top level parameters section of the template
and must be assigned a value at runtime, although default value is acceptable.

Supported types are: string number list<number, Comma delimited list, aws specific types and system manager parameter types.

Other fields in the template can call out these parameters using the `!Ref` intrinsic function.

In YAML, this would like like:

## Outputs  
Gets access to info about resources within a stack. We can get the Public IP or DNS for a EC2 Instance that was created.

**These outputs can be cross-referenced between stacks too!**

Documentation at https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html
