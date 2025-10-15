import os
import sqlite3 as sql


def _db_path():
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(base_dir, 'database', 'data_source.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)  # ensure parent dir exists
    return db_path


def _connect():
    con = sql.connect(_db_path(), timeout=10)
    return con


def listMessages():
   
    con = _connect()
    con.row_factory = sql.Row
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM messages;")
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        con.close()


def listusers():
    con = _connect()
    try:
        cur = con.cursor()
        users = cur.execute("SELECT Full_Name, Password FROM users").fetchall()
        return users
    finally:
        con.close()


def adduser(Full_Name, Password, Email):
    con = _connect()
    try:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (Full_Name, Password, Email) VALUES (?, ?, ?)",
            (Full_Name, Password, Email),
        )
        con.commit()
    finally:
        con.close()


def get_messages_by_chat(chat_id):
    con = _connect()
    con.row_factory = sql.Row
    try:
        cur = con.cursor()
        data = cur.execute(
            """
            SELECT users.Full_Name, messages.`Message Content`,
            messages.Time, messages.id
            FROM messages
            LEFT JOIN users ON messages.customerid = users.customerid
            WHERE messages.Chat = ?
            ORDER BY messages.Time ASC, messages.id ASC
            """,
            (chat_id,),
        ).fetchall()
        return data
    finally:
        con.close()


def add_message(full_name, content, chat_id, time):
    con = _connect()
    try:
        cur = con.cursor()


        user_query = "SELECT customerid FROM users WHERE Full_Name = ?"
        user_data = cur.execute(user_query, (full_name,)).fetchone()
        customerid = user_data[0] if user_data else None

        insert_query = """
            INSERT INTO messages
            (customerid, `Message Content`, Chat, Time)
            VALUES (?, ?, ?, ?)
        """
        cur.execute(insert_query, (customerid, content, chat_id, time))
        con.commit()
    finally:
        con.close()


def get_latest_message(chat_id):
    con = _connect()
    try:
        cur = con.cursor()
        data = cur.execute(
            """
            SELECT users.Full_Name, messages.`Message Content`
            FROM messages
            LEFT JOIN users ON messages.customerid = users.customerid
            WHERE messages.Chat = ?
            ORDER BY messages.Time DESC, messages.id DESC
            LIMIT 1
            """,
            (chat_id,),
        ).fetchone()
        if data:
            name, content = data
            preview = f"{name or 'Anonymous'}: {content}"
            if len(preview) > 30: 
                preview = preview[:27] + "..."
            return preview
        return "No messages yet"
    finally:
        con.close()
