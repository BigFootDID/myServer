from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    # 클라이언트 정보 추출
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    
    # 로그 파일에 기록 (append 모드)
    with open("access.log", "a", encoding="utf-8") as f:
        f.write(f"IP: {ip}, UA: {ua}\n")

    return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)
