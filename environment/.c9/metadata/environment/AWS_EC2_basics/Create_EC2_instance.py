{"filter":false,"title":"Create_EC2_instance.py","tooltip":"/AWS_EC2_basics/Create_EC2_instance.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":49,"column":82},"action":"insert","lines":["\"\"\"","This script manages Amazon EC2 instances using the Boto3 Python SDK","\"\"\"","# import stamtements","import boto3","","# create a EC2 resource and a instance name","ec2 = boto3.resource('ec2')","instance_name = 'lambdaEC2DailySnapshot'","","# store instance id","instance_id = None","","# Check whether the instance you're trying to create is already created","# and only work with an instance that hasn't been terminated","instances = ec2.instances.all()","instance_exist = False","","for instance in instances:","    for tag in instance.tags:","        if tag['Key'] == 'Name' and tag['Value'] == instance_name:","            instance_exist = True","            instance_id = instance.id","            print(f\"An instance named '{instance_name}' with the ID of '{instance_id}' already exists.\")","            break","    if instance_exist:","        break","","# Launch a new EC2 instance if it hasn't already been created","if not instance_exist:","    new_instance = ec2.create_instances(","        ImageId = 'ami-051f8a213df8bc089', # you can get this # from the EC2 console we you go to lauch a instance there","        MinCount = 1,","        MaxCount = 1,","        InstanceType = 't2.micro',","        KeyName = 'us-east-kp', # This is your key pair","        TagSpecifications = [","            {","                'ResourceType' : 'instance',","                'Tags' : [","                    {","                        'Key' : 'Name',","                        'Value' : instance_name # this is the name given before","                    },","                ]","            },","        ]","    )","    instance_id = new_instance[0].id","    print(f\"Instance named '{instance_name}' with ID '{instance_id}' is created.\")"],"id":1}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["2"],"id":2},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["C"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["E"]}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["-"],"id":3}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["-"],"id":4}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["S"],"id":5}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["S"],"id":6}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["_"],"id":7},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["E"]}],[{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["C"],"id":8},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["2"]}],[{"start":{"row":8,"column":40},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":8,"column":40},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":10}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":49,"column":82},"end":{"row":49,"column":82},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1725065236612,"hash":"0712219c795f7c8f7b19ebcb9039dc5d3329f05e"}