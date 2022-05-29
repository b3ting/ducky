:)


## Start up

1. pip3 install -r requirements.txt
2. DATABASE_URL=postgres://snfzjbzottankj:863d78821e6ea8be9a60abe9fd829eed951cbcf100707bb3861ea0667c7df423@ec2-44-196-174-238.compute-1.amazonaws.com:5432/d8fitsasagpcfa gunicorn --worker-class eventlet -w 1 wsgi:app