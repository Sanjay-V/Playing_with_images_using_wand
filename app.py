import os
from flask import Flask, request, render_template, send_from_directory, request, redirect, url_for, abort
from wand.image import Image
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    for upload in request.files.getlist("file"):
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
    return render_template("index.html", image_name=filename)

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/<photo>info")
def reading_images(photo):
    target = os.path.join(APP_ROOT, 'images/')
    image = os.listdir(target)
    if photo in image:
      with Image(filename = target + "/"+ photo) as img: 
        b = img.width
        c = img.height
        d = b + c
    return render_template("index.html", output=b)

if __name__ == "__main__":
    app.run(port=5555, debug=True)