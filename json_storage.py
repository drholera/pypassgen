import json
import os


class JsonStorage(object):

    file = 'passwords.json'

    def __init__(self):
        self.add_to_file('asd', 'ad')

    def add_to_file(self, password, date):
        # Create file if not exists
        if not os.path.exists(self.file):
            open(self.file, 'w').close()

        with open(self.file, 'r') as f:
            if os.path.getsize(self.file) == 0:
                file_content = None
            else:
                file_content = json.load(f)

        data = {'generated_passwords': []}

        if file_content and file_content['generated_passwords'][0]:
            data['generated_passwords'].append(file_content['generated_passwords'][0])

        data['generated_passwords'].append({
            'password': password,
            'date': date,
        })

        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)


json_test = JsonStorage()
