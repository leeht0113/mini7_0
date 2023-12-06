function sendMessage() {
    var question = document.getElementById("question").value; // 질문을 가져옴
    // 여기에 채팅창에 질문을 보내는 코드를 추가할 수 있습니다.
    // 예를 들어, ChatGPT에게 질문을 보내고 답변을 받아와서 채팅창에 추가하는 방식 등이 있습니다.
  }
  
  // 질문 버튼 클릭 이벤트
  document.getElementById("text-button").addEventListener("click", function(event) {
    event.preventDefault(); // 폼의 기본 동작(페이지 새로고침) 방지
    var question = document.getElementById("question").value;
    if (question.trim() !== '') {
      // 여기에 사용자가 질문을 보내는 함수 호출을 추가할 수 있습니다.
      sendMessage();
    }
  });
  
  // 채팅창 보이기/숨기기 토글
  function toggleChat() {
    var chatContainer = document.getElementById("chatContainer");
    if (chatContainer.style.display === "none") {
      chatContainer.style.display = "block";
    } else {
      chatContainer.style.display = "none";
    }
  }