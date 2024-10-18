import psycopg2

try:
    conn = psycopg2.connect(
        host="pgvector-latest.onrender.com",
        database="mydatabase",
        user="myuser",
        password="mypassword",
        port="5432"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
