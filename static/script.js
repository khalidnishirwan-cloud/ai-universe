// إرسال الرسالة
function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value;

    if (!message) return;

    addMessage(message, "user");

    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot");
    });

    input.value = "";
}

// إضافة الرسالة في صندوق الدردشة
function addMessage(text, type) {
    const chatBox = document.getElementById("chat-box");

    const div = document.createElement("div");
    div.className = "message " + type;
    div.innerText = text;

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// مسح المحادثة الحالية
function newChat() {
    document.getElementById("chat-box").innerHTML = "";
}

// توجيه المستخدم لصفحة تسجيل الدخول
function goLogin() {
    // افتح صفحة تسجيل الدخول عند توفرها
    window.location.href = "/login";
}

// توجيه المستخدم لصفحة إنشاء الحساب
function goRegister() {
    window.location.href = "/register";
}
