from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>AI Universe</title>
<style>
body { font-family: Arial; background: #202123; color: #e5e5e5; display: flex; justify-content: center; align-items: center; height: 100vh; }
.chat-container { width: 90%; max-width: 600px; background: #2a2a2e; border-radius: 10px; display: flex; flex-direction: column; padding: 20px; }
#chat-box { flex: 1; overflow-y: auto; padding: 10px; background: #1e1e1f; border-radius: 5px; margin-bottom: 10px; }
.input-area { display: flex; }
input { flex: 1; padding: 10px; border-radius: 5px 0 0 5px; border: none; outline: none; background: #3a3a3c; color: white; }
button { padding: 10px; border: none; background: #0a84ff; color: white; border-radius: 0 5px 5px 0; cursor: pointer; }
button:hover { background: #0066cc; }
p { margin: 5px 0; }
.user { color: #ffffff; }
.bot { color: #0a84ff; }
</style>
</head>
<body>
<div class="chat-container">
<h2>AI Universe</h2>
<div id="chat-box"></div>
<div class="input-area">
<input id="user-input" placeholder="اكتب رسالتك هنا...">
<button onclick="sendMessage()">إرسال</button>
</div>
</div>
<script>
function sendMessage() {
  let input = document.getElementById("user-input");
  if(input.value.trim() === "") return;
  let msg = input.value;
  input.value = "";
  let chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += "<p class='user'>👤 " + msg + "</p>";
  fetch("/send", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  })
  .then(res => res.json())
  .then(data => {
    chatBox.innerHTML += "<p class='bot'>🤖 " + data.reply + "</p>";
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/send", methods=["POST"])
def send():
    user_msg = request.json.get("message", "")
    reply = "🤖 رد تجريبي: " + user_msg
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
