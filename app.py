from flask import Flask,render_template, request

app = Flask(__name__)

def encrypt(message,key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key)% 26 + base 
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message,key):
    return encrypt(message,-key)

@app.route('/',methods = ["GET","POST"])
def index():
    output = None
    if request.method == "POST":
        mode = request.form.get("mode","").lower()
        text = request.form.get("text","")
        try:
            key = int(request.form.get("key",0))
            if mode in ("E","e"):
                output = encrypt(text,key)
            elif mode in ("D","d"):
                output = decrypt(text,key)
            else:
                output = "Invalid mode selected"
        except ValueError:
            output = "Invalid key:please enter a number between 1 to 25"
    return render_template("index.html",output=output)

    

if __name__ == '__main__':
    app.run(debug=True)