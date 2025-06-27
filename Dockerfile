FROM public.ecr.aws/lambda/python:3.13

# Install build tools needed for sentencepiece and others
RUN dnf install -y zip cmake gcc-c++ make pkgconf-pkg-config    

# Set working directory to /lambda
WORKDIR /lambda

# Copy requirements
COPY requirements-docker.txt .

# Install Python packages into 'python' directory
RUN pip install -r requirements-docker.txt -t python

# Create ZIP archive of the 'python' folder
RUN zip -r lambda-layer.zip python
    