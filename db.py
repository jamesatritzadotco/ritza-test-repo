import psycopg2

dbusername = "admin"
dbpassword = "8095uohoiw4ur90"
dbhost = "db-postgres-nyc1-1111-do-user-111111-0.db.ondigitalocean.com"
dbport = 25060
dbdatabase = "defaultdb"
dbsslmode = "require"

def connect():
    return psycopg2.connect(
        user=dbusername,
        password=dbpassword,
        host=dbhost,
        port=dbport,
        database=dbdatabase,
        sslmode=dbsslmode
    )
