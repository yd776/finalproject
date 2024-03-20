from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def display_images():
    image_paths = [
        "C:\\Users\\yashas\\final_project\\frames\\frame_0007Snapchat.mp4.jpg",
"C:\\Users\\yashas\\final_project\\frames\\frame_0126Snapchat.mp4.jpg",
"C:\\Users\\yashas\\final_project\\frames\\frame_0127Snapchat.mp4.jpg"

    ]

    return render_template('index.html', image_paths=image_paths)

@app.route('/image/<path:image_path>')
def get_image(image_path):
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
