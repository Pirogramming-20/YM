function clickChat() {
  console.log("클릭");
  if (document.querySelector(".show").id == "showChat") {
    document.querySelector(".show").id = "noShowChat";
  } else {
    document.querySelector(".show").id = "showChat";
  }
}
// const room_num = "{{ room.id }}";
//     const room_name = "{{ room.room_name }}";
//     const username = "{{ user.username }}";
      console.log(room_num);
      console.log(room_name);
      console.log(username);


let socket = io.connect(
  location.protocol + "//" + document.domain + ":" + location.port
);
socket.emit("join", room_name);

// 소켓서버에서 받은 데이터를 기반으로 html에 코드 추가
socket.on('message', function(data) {
  console.log('Message received: ', data);

  // Create the main chat item container
  let chatItem = document.createElement('div');
  chatItem.className = 'chat';

  // Create and append the user div
  let userDiv = document.createElement('div');
  userDiv.className = 'user';
  userDiv.textContent = data[1]; // Assuming data[1] contains the username
  chatItem.appendChild(userDiv);

  // Create and append the message div
  let messageDiv = document.createElement('div');
  messageDiv.className = 'message';
  messageDiv.textContent = data[0]; // Assuming data[0] contains the message
  chatItem.appendChild(messageDiv);

  // Create the list item and append the chat item to it
  let listDiv = document.createElement('div');
  if (data[1] === username) {
    listDiv.className += ' my_chat'; // Note the space before the class name
  }
  listDiv.appendChild(chatItem);

  // Append the list item to the messages list
  document.getElementById('messages').appendChild(listDiv);
});

// 메시지 전송버튼이 눌렸을때 입력된 메세지를 소켓을 통해 보내고 메세지 입력창을 비움
function click1() {
  console.log("clk");
  let text = document.getElementById("input").value;
  console.log("clk2");
  socket.emit("message", text, username, room_name);
  document.getElementById("input").value = "";
}
document
  .getElementById("input")
  .addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {
      // 'Enter'키의 keyCode는 13입니다.
      let text = e.target.value;

      socket.emit("message", text, username, room_name);
      e.target.value = "";
    }
  });