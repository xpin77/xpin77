from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simulasi database pengguna (username dan password)
users = {
    "admin": "password123",
    "user1": "mypassword"
}

# Template HTML untuk halaman login
login_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Website Sederhana</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f4f6;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-size: 18px;
        }

        .container {
            text-align: center;
            background-color: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 400px;
        }

        h1 {
            color: #4CAF50;
            font-size: 36px;
        }

        input[type="text"], input[type="password"] {
            padding: 10px;
            font-size: 18px;
            width: 80%;
            margin-top: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 20px;
            margin-top: 20px;
        }

        button:hover {
            background-color: #45a049;
        }

        .error {
            color: red;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
        {% if error %}
            <div class="error">
                <p>Username atau Password salah!</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

# Template HTML untuk halaman setelah login
welcome_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selamat datang</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f4f6;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-size: 18px;
        }

        .container {
            text-align: center;
            background-color: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 600px;
        }

        h1 {
            color: #4CAF50;
            font-size: 36px;
        }

        p {
            font-size: 24px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 20px;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Selamat datang, {{ username }}!</h1>
        <img src="https://vegas.nyc3.cdn.digitaloceanspaces.com/0072_y_st_webp-m/sticker-fan_14356931_m.webp" alt="Foto Profil" style="max-width: 100%; height: auto;">
        <p>Anda telah berhasil login.</p>
        <button onclick="window.location.href='/'">Logout</button>
        <p style="margin-top: 20px;">Pemilik: Xpin</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifikasi username dan password
        if users.get(username) == password:
            return render_template_string(welcome_html, username=username)
        else:
            return render_template_string(login_html, error=True)
    
    return render_template_string(login_html, error=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
