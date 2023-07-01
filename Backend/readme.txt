venv used: coreroot

postgres user: core
password: anishcore123#

superuser: anish
    pw: anish
    email: anish@anish.com

error: doing migrate while creating custom user model
InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency core_user.0001_initial on database 'default'.
solution:

https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory



{
	"username": "mouse21","first_name": "Mickey","last_name": "Mouse","password": "12345678","email": "mouse@yopmail.com"
}