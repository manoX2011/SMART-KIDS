Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول - SMART KIDS ACADEMY</title>
    <link rel="stylesheet" href="styles.css"> <!-- يمكنك وضع CSS الخاص بك في ملف منفصل -->
</head>
<body>
    <div class="login-container">
        <h2>تسجيل الدخول إلى SMART KIDS ACADEMY</h2>
        <form action="/login" method="POST">
            <div class="input-group">
                <label for="username">اسم المستخدم:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">كلمة المرور:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">تسجيل الدخول</button>
        </form>
    </div>
</body>
</html>

css
نسخ الكود
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.login-container {
    max-width: 400px;
    margin: 100px auto;
...     background-color: #fff;
...     padding: 20px;
...     border-radius: 5px;
...     box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
... }
... 
... h2 {
...     text-align: center;
...     margin-bottom: 20px;
... }
... 
... .input-group {
...     margin-bottom: 15px;
... }
... 
... .input-group label {
...     display: block;
...     margin-bottom: 5px;
... }
... 
... .input-group input {
...     width: 100%;
...     padding: 10px;
...     border: 1px solid #ccc;
...     border-radius: 3px;
... }
... 
... button {
...     width: 100%;
...     padding: 10px;
...     background-color: #007bff;
...     color: #fff;
...     border: none;
...     border-radius: 3px;
...     cursor: pointer;
... }
... 
... button:hover {
...     background-color: #0056b3;
