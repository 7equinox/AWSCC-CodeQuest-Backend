# app.py
# The 'src' package provides the Flask application instance
from src import app

# This condition verifies if the script is running directly or being imported
if __name__ == '__main__':
    # If the script is running directly, the Flask server is started
    # The server is configured to listen on all network interfaces (host='0.0.0.0') and port 5000
    # Debug mode is enabled for development purposes, and threading is disabled for simplicity
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
