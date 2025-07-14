set -e

host="db"
port=5432

echo "Waiting for postgres at $host:$port..."

while ! nc -z $host $port; do
  sleep 1
done

echo "Postgres is up - executing command"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
