# Use an official Python runtime as the base image
FROM python:3

# Copy the rest of the application code to the container
COPY GitAction_Zabbix /GitAction_Zabbix

# Install the Python dependencies
RUN pip install --no-cache-dir -r /GitAction_Zabbix/requirements.txt

# Set the working directory in the container
WORKDIR /GitAction_Zabbix

# Set the entry point command for the container
CMD [ "python", "main.py" ]
