const roomName = JSON.parse(document.getElementById("json-roomname").textContent)
const userName = JSON.parse(document.getElementById("json-username").textContent)
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/')
chatSocket.onmessage = function(e) {
    console.log('onmessage')
    const data = JSON.parse(e.data)
    if (data.message) {
        let html = `<p><strong>${data.username}</strong>: ${data.message}</p>`
        document.querySelector('#chat-messages').innerHTML += html

        scrollToBottom()
    } else {
        alert('The message was empty')
    }
}
chatSocket.onclose = function(e) {
    console.log('onclose')
}
//
document.querySelector('#chat-message-submit').onclick = function(e) {
    e.preventDefault()
    const messageInputDom = document.querySelector('#chat-message-input')
    const message = messageInputDom.value

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }))

    messageInputDom.value = ''

    return false
}
        //
function scrollToBottom() {
    const objDiv = document.querySelector('#chat-messages')
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom()