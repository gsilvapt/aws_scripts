# README

This directory contains sample CloudFormation Templates for demonstration purposes. 

CF is AWS's Infrastructure as Code tool designed for AWS. It is free to use, except the resources it generates that are 
paid.

CF allows to create, update and delete infraestructure resources. These templates are pushed to CF through S3, and that 
triggers the orchestrator.


We can use the same template to update resources - like adding tags after creation. CF figures out 
the delta on its own and updates de resources on its own. In the Console choose the **Update Stack Action**.

Stacks can be deleted from the console.

## Terminology  

* **Templates**: JSON/YAML formatted text file. It is the input for CloudFormation.
* **Stack**: When CF executes a template, it creates a stack with those resources. To update resources within a template, 
  we need to update the stack.
* **ChangeSet**: Before updating a stack, we can generate a change set. This would allow to see the impact our changes 
  would have in running resources. For example, renaming RDS implies create a new instance, delete the old one.
  
## Template Anatomy  
There are a handful of variables in a template:

* **AWSTemplateVersion**: Optional, to specify the CF Template format.
* **Description**: Optional string to describe a template.
* **Metadata**: Optional metadata vars we can set for a template
* **Parameters**: Optional set of params for runtime.
* **Mappings**: Optional set of key/values to work like a lookup-table.
* **Conditions**: Optional set to allow when resources are generated.
* **Transform**: Optional et of transforms that CF will use to process a template, including external scripts.
* **Resources**: The only required section.
* **Outputs**: Optional set of outputs to get after the templates were processed.
