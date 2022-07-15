# For more information, please refer to https://aka.ms/vscode-docker-python
FROM public.ecr.aws/lambda/python:3.8

ARG FUNCTION_DIR="/var/task/"

# Copy function code
COPY ./ ${FUNCTION_DIR}

# Setup Python environment
COPY requirements.txt  .
RUN pip install -r requirements.txt

# Grab the zappa handler.py and put it in the working directory
RUN ZAPPA_HANDLER_PATH=$( \
    python -c "from zappa import handler; print (handler.__file__)" \
    ) \
    && echo $ZAPPA_HANDLER_PATH \
    && cp $ZAPPA_HANDLER_PATH ${FUNCTION_DIR}


CMD [ "handler.lambda_handler" ]