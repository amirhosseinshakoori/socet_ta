## Server

- **Dependencies:** 
  - Python 3.x

- **Usage:**
  1. Run the server script (`server.py`) on a machine.
     ```bash
     python server.py
     ```
     This will start the server and make it listen for incoming client connections.

  2. The server listens on a specified host and port (default is 'localhost:12345'). You can customize these settings in the `start_server` function inside the `server.py` file.

  3. The server echoes back any data received from clients after decoding it from ASCII.

## Client

- **Dependencies:**
  - Python 3.x

- **Usage:**
  1. Run the client script (`client.py`) on another machine or locally.
     ```bash
     python client.py
     ```
     This will connect the client to the server.

  2. The client prompts the user to enter ASCII characters, sends them to the server, and then displays the echoed response from the server.

  3. The client can be interrupted by the user (Ctrl+C) to gracefully exit the program.

  4. The client's connection settings (host and port) can be customized in the `start_client` function inside the `client.py` file.

- **Notes:**
  - Make sure to have Python installed on both the server and client machines.
  - The code uses ASCII encoding for simplicity. If you need to support non-ASCII characters, consider using a different encoding, such as UTF-8.
  - This implementation is meant for educational purposes and may need further modifications for production use.
  - Feel free to experiment with the code and customize it according to your needs!

---

**Note:**
This code is part of the employment task for Asia Telecommunications company.
