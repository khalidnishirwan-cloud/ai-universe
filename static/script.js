function sendMessage(){
    let msg = document.getElementById("message").value;

    fetch("/ask",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:msg})
    })
    .then(res=>res.json())
    .then(data=>{
        let box=document.getElementById("chat-box");
        box.innerHTML+=`<p><b>أنت:</b> ${msg}</p>`;
        box.innerHTML+=`<p><b>AI:</b> ${data.response}</p>`;
    });

    document.getElementById("message").value="";
}

function newChat(){
    document.getElementById("chat-box").innerHTML="";
}
