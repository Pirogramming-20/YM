const room_num = document.getElementById("info_room_num").innerText;
const room_name = document.getElementById("info_room").innerText;
const username = document.getElementById("info_username").innerText;
console.log(room_num);
console.log(room_name);
console.log(username);

let socket = io.connect(
  location.protocol + "//" + document.domain + ":" + location.port
);
socket.emit("join", room_name);

// 소켓서버에서 받은 데이터를 기반으로 html에 코드 추가
socket.on("message", function (data) {
  console.log("msg");
  console.log(data);
  let li = document.createElement("li");
  li.append(
    document.createTextNode(data[1]),
    document.createTextNode(" : "),
    document.createTextNode(data[0])
  );
  document.getElementById("messages").appendChild(li);
});

// 메시지 전송버튼이 눌렸을때 입력된 메세지를 소켓을 통해 보내고 메세지 입력창을 비움
function click1() {
  console.log("clk");
  let text = document.getElementById("input").value;
  console.log("clk2");
  socket.emit("message", text, username, room_name);
  document.getElementById("input").value = "";
}
document.getElementById("input").addEventListener("keydown", function (e) {
  if (e.keyCode === 13) {
    // 'Enter'키의 keyCode는 13입니다.
    let text = e.target.value;

    socket.emit("message", text, username, room_name);
    e.target.value = "";
  }
});
