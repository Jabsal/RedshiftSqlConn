def copy_s3_to_redshift():

    conn = psycopg2.connect(dbname={REDSHIFT_DATABASE}, host={REDSHIFT_HOST}, user={REDSHIFT_USER}, password={REDSHIFT_PASSWORD})
    cur = conn.cursor();

    # Begin transaction
    cur.execute("begin;")

    cur.execute("copy book from 's3://book-migration/book.csv' credentials 'aws_access_key_id={ACCESS_KEY};aws_secret_access_key={SECRET_KEY}' csv;")
    
	# Commit transaction
    cur.execute("commit;")
	
    print("Copy executed fine!")

copy_s3_to_redshift();
