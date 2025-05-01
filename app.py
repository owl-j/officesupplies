from flask import Flask, request, jsonify

app = Flask(__name__)

milk_status = "We have milk! 🥛"

@app.route("/milk", methods=["POST"])
def milk():
    text = request.form.get("text", "").strip().lower()
    user = request.form.get("user_name")

    global milk_status

    if text == "out":
        milk_status = f"🚫 We're out of milk! Reported by @{user}."
    elif text == "restocked":
        milk_status = f"✅ Milk has been restocked! Thanks @{user}!"
    elif text == "" or text == "status":
        pass
    else:
        return jsonify({
            "response_type": "ephemeral",
            "text": "Usage: `/milk [status|out|restocked]`"
        })

    return jsonify({
        "response_type": "in_channel",
        "text": milk_status
    })

@app.route("/")
def index():
    return "Milk Tracker is running!"

if __name__ == "__main__":
    app.run()
