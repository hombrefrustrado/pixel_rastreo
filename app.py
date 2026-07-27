from flask import Flask, send_file, request 
import logging
app = Flask(__name__)

@app.route("/pixel.jpg")
def pixel():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip:
        ip = ip.split(",")[0].strip()

    user_agent = request.headers.get("User-Agent", "Desconocido")

    app.logger.info(f"IP: {ip} | User-Agent: {user_agent}")

    return send_file(
        "battie.jpg",
        mimetype="image/jpg",
        max_age=0
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)