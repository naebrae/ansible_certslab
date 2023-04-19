#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import psycopg2
import pprint

def getPGUser(connString):
    try:
        conn = psycopg2.connect(connString)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pg_user")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        sys.exit(-1)
    return 0

def main():
    records = getPGUser("sslcert=vagrantcln.crt sslkey=vagrantcln.key sslmode=verify-ca host=crtsrv user=vagrant dbname=postgres")
    pprint.pprint(records)    

if __name__ == "__main__":
    sys.exit(main())
