from flask import Flask, render_template

app = Flask(__name__)

photos = {
    "ABC123": {
        "photo_url": "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0013260531005940/result.jpg",
        "strip_url": "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0013260531005940/result.jpg"
    }
}

@app.route("/p/<session_id>")
def landing(session_id):

    photos = [
        "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0013260531005940/result.jpg",
        "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0010260530213226/result.jpg",
        "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0010260530220431/result.jpg"
    ]

    if not photos:
        return "Photo not found", 404

    return render_template(
        "landing.html",
        session_id=session_id,
        photos=photos
    )

if __name__ == "__main__":
    app.run(debug=True)