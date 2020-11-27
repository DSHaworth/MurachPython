# https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

from gpiozero import PWMLED
from flask import Flask, render_template, request

# Create a flask object
app = Flask(__name__, template_folder='templates')

# Create a PWMLED object for each color
ledRed = PWMLED(4)
ledGreen = PWMLED(17)
ledBlue = PWMLED(27)

rgb = {'red': 1, 'green': 1, 'blue': 1}

def changeColor(rgb):
    print(rgb)

    ledRed.value = rgb["red"]
    ledGreen.value = rgb["green"]
    ledBlue.value = rgb["blue"]

@app.route("/")
def main():
   return render_template('main.html')

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<action>", methods = ["POST"])
def control(action):
    
    if action == "rgbLED":
        rgb = {'red': (255 - int(request.json['red']))/255, 'green': (255 - int(request.json['green']))/255, 'blue': (255 - int(request.json['blue']))/255}
        changeColor(rgb)
        return str({"OK": "OK"})        

if __name__ == "__main__":
    changeColor(rgb)
    app.run(host='0.0.0.0', port=1024, debug=True)