from flask import Flask, request, jsonify
from naoqi import ALProxy, ALModule, ALBroker

app = Flask(__name__)

nao_IP = "192.168.1.104"
nao_port = 9559

tts = ALProxy("ALTextToSpeech", nao_IP, nao_port)
# tts.setVolume(1.5)  # Define volume of the robot
animatedSpeech = ALProxy("ALAnimatedSpeech", nao_IP, nao_port)

# Set the volume and speed of the speech
tts.setVolume(2)  # Set volume between 0.0 and 1.0
tts.setParameter("speed", 65)  # Set speed (default is 100%)

# Define body language mode (full, disabled, or random)
configuration = {"bodyLanguageMode": "contextual"}  # Options: "random", "disabled", "contextual"


@app.route("/talk", methods=["POST"])
def talk():
    print("Received a request to talk")
    message = request.json.get("message")  # Get the message from the request
    if message:
        animatedSpeech.say(str(message), configuration)  # Use animated speech to talk
        return jsonify(success=True)
    else:
        return jsonify(success=False, error="No message provided"), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)  # Run the Flask server
