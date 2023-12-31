css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}

section[data-testid="stSidebar"] {
    width: 40% !important;
}

[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        {{IMG}}
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''