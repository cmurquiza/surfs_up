# Import the Flask dependency 
from flask import Flask

# Creating a new Flask app instance
app = Flask(__name__)

# Defining the starting point known as the root

@app.route('/')
def hello_world():
    return 'Hello world'

# Run code
if __name__ == "__main__":
    app.run(debug=True)