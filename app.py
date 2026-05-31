from flask import Flask, render_template
from sqlalchemy import text

from db import DB
from models import PhotoBoothMain

app = Flask(__name__)

@app.route("/p/<session_id>")
def landing(session_id):

    photos = [
        "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0013260531005940/result.jpg",
        "https://pub-0dfaa927561b49c8a0b5b103428dd44c.r2.dev/2026/BS001/BS0010260530220431/result.jpg"
    ]

    if not photos:
        return "Photo not found", 404

    return render_template(
        "landing.html",
        session_id=session_id,
        photos=photos
    )

@app.route("/d/<session_id>")
def landing_db(session_id):
    db = DB.session()
    try:
        photos = [
            row.download_url
            for row in (
                db.query(PhotoBoothMain.download_url)
                  .filter(PhotoBoothMain.session_id == session_id)
                  .all()
            )
            if row.download_url
        ]

    finally:
        db.close()

    if not photos:
        return render_template(
        "error.html",
        session_id=session_id,
        photos=photos
    )


    return render_template(
        "landing.html",
        session_id=session_id,
        photos=photos
    )


@app.route("/test-db")
def test_db():

    db = DB.session()

    try:

        result = db.execute(text("SELECT NOW()"))

        return str(result.scalar())

    finally:

        db.close()

@app.route("/check/<session_id>")
def check(session_id):

    db = DB.session()

    try:

        rows = (
            db.query(PhotoBoothMain)
              .filter(
                  PhotoBoothMain.session_id == session_id
              )
              .all()
        )

        return {
            "count": len(rows),
            "files": [
                row.download_url
                for row in rows
            ]
        }

    finally:

        db.close()

if __name__ == "__main__":
    app.run(debug=True)