# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")  # 允许跨域

@app.route('/wall')
def wall():
    return render_template('wall.html')  # 大屏幕页面

@app.route('/')
def index():
    return render_template('index.html')  # 学生扫码输入页面

# 接收学生发送的弹幕
@socketio.on('send_message')
def handle_message(data):
    username = data.get('username', '匿名')
    content = data.get('content', '')
    emit('new_message', {'username': username, 'content': content}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, allow_unsafe_werkzeug=True)

