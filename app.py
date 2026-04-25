from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

# 🔹 สร้าง session ใหม่
@app.route("/session", methods=["POST"])
def create_session():
    conn = get_conn()
    cur = conn.cursor()

    code = request.json.get("session_code")

    cur.execute(
        "INSERT INTO sessions (session_code) VALUES (%s) RETURNING id",
        (code,)
    )
    session_id = cur.fetchone()[0]

    # สร้าง queue
    cur.execute(
        "INSERT INTO queue (session_id, status) VALUES (%s, 'waiting')",
        (session_id,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"session_id": session_id})


# 🔹 เพิ่มรูป
@app.route("/photo", methods=["POST"])
def add_photo():
    conn = get_conn()
    cur = conn.cursor()

    session_code = request.json.get("session_code")
    file_url = request.json.get("file_url")

    cur.execute(
        "SELECT id FROM sessions WHERE session_code=%s",
        (session_code,)
    )
    session = cur.fetchone()

    if not session:
        return jsonify({"error": "session not found"}), 404

    session_id = session[0]

    cur.execute(
        "INSERT INTO photos (session_id, file_url) VALUES (%s, %s)",
        (session_id, file_url)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "ok"})


# 🔹 ดูรูปทั้งหมด
@app.route("/photos/<code>")
def get_photos(code):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.file_url
        FROM photos p
        JOIN sessions s ON p.session_id = s.id
        WHERE s.session_code=%s
    """, (code,))

    photos = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return jsonify({"photos": photos})


# 🔹 เช็คสถานะ queue
@app.route("/queue/<code>")
def get_queue(code):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT q.status
        FROM queue q
        JOIN sessions s ON q.session_id = s.id
        WHERE s.session_code=%s
    """, (code,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    return jsonify({"status": result[0] if result else "not found"})


# 🔹 update queue (admin / system)
@app.route("/queue/update", methods=["POST"])
def update_queue():
    conn = get_conn()
    cur = conn.cursor()

    code = request.json.get("session_code")
    status = request.json.get("status")

    cur.execute("""
        UPDATE queue
        SET status=%s, updated_at=NOW()
        WHERE session_id = (
            SELECT id FROM sessions WHERE session_code=%s
        )
    """, (status, code))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "updated"})


if __name__ == "__main__":
    app.run()