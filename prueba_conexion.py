import pymysql
#prueba conexion de railway con mi bd

conn = pymysql.connect(
    host="maglev.proxy.rlwy.net",
    port=40511,
    user="root",
    password="tpqMFyzStiOfMNEeLXcTsLagIWSAkuRr",
    database="railway"
)

print("✅ Conexión exitosa")
conn.close()