#!/usr/bin/env python
import datetime
import os
import sys

if __name__ == "__main__":

    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bloodrush.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    # Import the required Django modules
    import django
    from django.conf import settings

    # Initialize Django
    django.setup()


    # Backup function
    def backup_database():
        try:
            # Create a backup folder if it doesn't exist
            backup_folder = 'database_backups'
            if not os.path.exists(backup_folder):
                os.makedirs(backup_folder)

            # Generate a unique filename based on the current timestamp
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            backup_file = f'{backup_folder}/backup_{timestamp}.sql'

            # PostgreSQL dump command to create plain SQL backup
            db_settings = settings.DATABASES['default']
            db_name = db_settings['NAME']
            db_user = db_settings['USER']
            db_password = db_settings['PASSWORD']
            db_host = db_settings['HOST']
            db_port = db_settings['PORT']
            backup_command = f'pg_dump -U {db_user} -h {db_host} -p {db_port} -Fp -f {backup_file} {db_name}'
            os.system(backup_command)

            return f'Backup created successfully! File path: {backup_file}'

        except Exception as e:
            return f'Error creating backup: {str(e)}'


    # Import function
    def import_backup(backup_file):
        try:
            # PostgreSQL import command using psql
            db_settings = settings.DATABASES['default']
            db_user = db_settings['USER']
            db_name = db_settings['NAME']
            db_host = db_settings['HOST']
            db_port = db_settings['PORT']
            import_command = f'psql -U {db_user} -h {db_host} -p {db_port} -d {db_name} -f {backup_file}'
            os.system(import_command)

            return 'Backup imported successfully!'

        except Exception as e:
            return f'Error importing backup: {str(e)}'


    # Call the backup function
    # backup_result = backup_database()
    # print(backup_result)

    # Call the import function
    import_result = import_backup('database_backups/backup_2023-06-26_17-58-42.sql')
    print(import_result)