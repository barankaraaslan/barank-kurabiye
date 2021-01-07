rm db.sqlite3
rm -r be/migrations
./manage.py makemigrations be
./manage.py migrate
