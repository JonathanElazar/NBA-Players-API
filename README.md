# 🏀 NBA Players API

A simple REST API for retrieving NBA player statistics. This project is designed to help developers easily integrate player data into their own applications, websites, and projects.

## 📖 Documentation

Full API documentation is available here:

**https://github.com/JonathanElazar/NBA-Players-API/blob/main/docs.md**

---

# 🌐 Public API Server

The public API is currently available at:

**https://eswzb3ycjm.localto.net/**

> **Note**
>
> This server is hosted using the free version of LocaltoNet. When making requests, you should include the `localtonet-skip-warning` header to bypass the LocaltoNet warning page.

### Example

Without the header:

```bash
curl "https://eswzb3ycjm.localto.net/name/jaylen/brown"
```

Recommended:

```bash
curl -H "localtonet-skip-warning: 1" \
"https://eswzb3ycjm.localto.net/name/jaylen/brown"
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/JonathanElazar/NBA-Players-API.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Server

There are two ways to run the API.

## Option 1: Flask (Development)

Run the server using Flask:

### Windows

```bash
py main.py
```

### Linux/macOS

```bash
python3 main.py
```

> **Warning**
>
> Flask's built-in server is intended **only for development**. Do not use it in production.

### Enable Debug Mode

To enable Flask's debugger, change:

```python
app.run("0.0.0.0", 5000)
```

to:

```python
app.run("0.0.0.0", 5000, debug=True)
```

---

## Option 2: Waitress (Production)

For production deployments, use Waitress:

```bash
waitress-serve --host=0.0.0.0 --port=5000 main:app
```

Waitress is recommended because it is a production-ready WSGI server.

**Note:**

* No interactive debugger
* No automatic code reloading
* More secure and stable than Flask's built-in server

---

# 📡 Example Request

```bash
curl -H "localtonet-skip-warning: 1" \
"https://eswzb3ycjm.localto.net/name/lebron/james"
```

---

# 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

Feel free to open an issue or submit a pull request.
