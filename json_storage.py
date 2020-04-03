import json
import os


class JsonStorage(object):
    """ Json manipulations """

    file = 'passwords.json'

    def add_to_file(self, password, date):
        # Create file if not exists.
        if not os.path.exists(self.file):
            open(self.file, 'w').close()

        # Receiving file content.
        with open(self.file, 'r') as f:
            if os.path.getsize(self.file) == 0:
                file_content = None
            else:
                file_content = json.load(f)

        # File content initialization.
        data = {'generated_passwords': []}

        if file_content and file_content['generated_passwords']:
            data = file_content

        data['generated_passwords'].append({
            'password': password,
            'date': date,
        })

        # Save data as JSON.
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)
