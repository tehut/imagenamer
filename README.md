## Get up and dev-ing

1. Clone this repository
2. Build the image locally 
  - ` docker build . -t imagenamer`
3. Run the image and mount the imagenamer directory from your dev computer directly to the container. This will allow you to share the directory across both your dev machine and our test environment.
  - `docker run -v $(pwd):/home/imagenamer`
4. Configure git in the test environment (I will probably script this into the entrypoint script for us sometime tomorrow so you can just pass your username in on docker run but for now we'll do it manually)
  - `git config --global user.email "your git email"
5. Profit
  - make changes in the image directory and see them show up inside the container

