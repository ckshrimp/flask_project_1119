# contact.py
from flask import Blueprint, jsonify, render_template, request
from openai import OpenAI

home_bp = Blueprint('home', __name__)
client = OpenAI(api_key='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')


@home_bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@home_bp.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message')
    print(f"Received message: {user_message}")


    # 呼叫 OpenAI API 生成回應
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 或 "gpt-4" 根據你的 API 訂閱情況
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = response.choices[0].message.content
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        bot_response = "抱歉，我無法處理您的請求。請稍後再試。"


    return jsonify({'response': bot_response})