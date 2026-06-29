# NBA Players API
This is an api I made allowing programmers to get NBA players stats for there own projects. See the docs at https://github.com/JonathanElazar/NBA-Players-API/blob/main/docs.md 
## Installing The Program
### Use the following commands to install
1. `git clone https://github.com/JonathanElazar/NBA-Players-API.git`
2. `pip install -r requirements.txt`

## Running The Server
There are two ways to run the server the easiest way is with normal flask while the more secure way is with waitress.
### Running with flask
simply use `py main.py` on windows or `python3 main.py` on linux.
Only use this for development purposes never for deployment.
If you run with flask you can edit the code at the bottom
For debuger edit
```python
app.run("0.0.0.0", 5000)
```
to:
```python
app.run("0.0.0.0", 5000, debug=True)
```
### Running with waitress
Use `waitress-serve --host=0.0.0.0 --port=5000 main:app`
This wont have any logs or debugger but it will securly deploy the server on port 5000.
