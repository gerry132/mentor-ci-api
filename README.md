# mentor-ci-api - Run Api Server

## Requirements
1. Git Bash if using Windows
2. Python

## Running the API Server
1. Install requirements from requirements.txt: Open git bash, or VS Code terminal, use the cd command to change directory: e.g cd ~/gerry/workspace/ci_demo/basicapi.
   At this point, run pip install -r requirements.txt
2. You should then be able to run python manage.py runserver (make sure you're in the folder that contains manage.py. You can type ls in the command line to view files in your current folder)
3. If all goes well, you should see the server running on http://127.0.0.1:8000/, which you can view in your browser.

## Running Clients
1. You can copy and paste the curl commands from the curl-client.sh into your terminal and you should see your JSON being rendered.
2. To run the Python client, type python python_client.py into the terminal and hit enter.
3. To run the web client, run python -m http.server 8080 and go to http://127.0.0.1:8080/ in your browser.

