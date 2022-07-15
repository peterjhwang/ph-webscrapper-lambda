# Serverless Web Apps with Docker & Zappa

## Building the Docker image
1. Run `zappa save-python-settings-file production -o zappa_settings.py` to generate & save the Python settings file required by Zappa
2. Build the Docker image with `docker build -t ph-webscrapper:latest .`
3. To run on your local machine `docker run -p 9000:8080 ph-webscrapper:latest`
4. To locally test, run this command. `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"path": "/test", "httpMethod": "GET", "requestContext": {}, "body": null}'`
5. Create a new ECR repository by running `aws ecr create-repository --repository-name ph-webscrapper --image-scanning-configuration scanOnPush=true`
6. Authenticate your local machine so it can push images to your repostiroy by running `aws ecr get-login-password | docker login --username AWS --password-stdin <your_registry_id>.dkr.ecr.ap-southeast-2.amazonaws.com`
7. Point your Docker image to your new repository `docker tag ph-webscrapper:latest <your_registry_id>.dkr.ecr.ap-southeast-2.amazonaws.com/ph-webscrapper:latest`
8. And push it `docker push <your_registry_id>.dkr.ecr.ap-southeast-2.amazonaws.com/ph-webscrapper:latest`


## Deploying with Zappa

Deploying the lambda function with your new Docker image can be accomplished by using the `zappa deploy` command and passing in the Docker image URI:

`zappa deploy ph-webscrapper -d <your_registry_id>.dkr.ecr.ap-southeast-2.amazonaws.com/ph-webscrapper:latest`