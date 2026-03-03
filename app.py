from flask import Flask, request, redirect, url_for

app = Flask(__name__)

PASSWORD = "KING HERE"

def check_auth(username, password):
    return password == PASSWORD

def authenticate():
    return '''
    <h2>Private AI Reel Studio 🔐</h2>
    <form method="POST">
        <input type="password" name="password" placeholder="Enter Password"/>
        <button type="submit">Login</button>
    </form>
    '''

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password")
        if password == PASSWORD:
            return """
            <h1>Welcome King 👑🔥</h1>
            <p>AI Reel Studio Running Successfully</p>
            """
        else:
            return "<h3>Wrong Password ❌</h3>" + authenticate()
    return authenticate()

if __name__ == "__main__":
    app.run()
