# 🏀 NBA Players API
NBA Players API is a REST API for retrieving data about NBA players. Try it at https://eswzb3ycjm.localto.net/

<img width="633" height="269" alt="image" src="https://github.com/user-attachments/assets/572afc28-0f27-43ee-b2cf-bb88aeb9a374" />

## 💻 API Usage Example
To get info about any player, lets say Michael Jordan you can use the command
```bash
curl -H "localtonet-skip-warning: 1" "https://eswzb3ycjm.localto.net/name/michael/jordan"
```
This should respond json info about the player if so than congradulations you just used the API for info about Michael Jordan. Make sure you check out the docs at https://github.com/JonathanElazar/NBA-Players-API/blob/main/docs.md

## 🖥️ Host Server
There are a few different ways to host the server. The first option is with flask this is very good for development if contributing to the open source code but isn't secure or stable for production. If you are hosting the server for production you should use waitress which is made for production.

### Run with Flask
To run with flask you can simplily run with python.
Use this command to download dependencies
```bash
pip install -r requirements.txt
```
If your on windows you will than use:
```bash
py main.py
```
And if your on linux/macOS you will use:
```bash
python3 main.py
```
Just so you know if you go to the last line that says:
```python
app.run("0.0.0.0", 5000)
```
You can change that to:
```python
app.run("0.0.0.0", 5000, debug=True)
```
to turn on debug mode.
### Run with Waitress
To run the server with waitress start with
```bash
pip install -r requirements.txt
```
Than use the command
```bash
waitress-serve --host=0.0.0.0 --port=5000 main:app
```
to start running.
If you would like to implement rate limiting when serving for production you can to the line that says
```python
needs_ratelimiting = False  # Set to True to enable rate limiting, False to disable it
```
and change the value to true.
