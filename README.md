# Get up and dev-ing

1. Clone this repository
2. Build the image locally 
  - ` docker build . -t imagenamer`
3. Run the image and mount the imagenamer directory from your dev computer directly to the container. This will allow you to share the directory across both your dev machine and our test environment.
  - Linux/BSD: `docker run -it -v $(pwd):/home/imagenamer imagenamer /bin/bash`
  - Windows PowerShell: `docker run -it -v ${pwd}:/home/imagenamer imagenamer /bin/bash`
4. Configure git in the test environment (I will probably script this into the entrypoint script for us sometime tomorrow so you can just pass your username in on docker run but for now we'll do it manually)
  - `git config --global user.email "your git email`
5. Profit
  - make changes in the image directory and see them show up inside the container

6. Connect to AWS
  - `aws configure`
  -- Enter api key and secret
  -- Region: `us-east-1`
  -- Format: `json`
  - Example AWS commands
  -- Get s3 buckets: `aws s3 ls`
  -- List items in bucket _i_: `aws s3 ls _i_`
  -- Copy item locally to bucket _i_: `aws s3 cp _path_ s3://_i_/_path_`
  -- Sync site: `aws s3 sync /home/imagenamer/site/. s3://_i_/.`
