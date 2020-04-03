import random, string, sys
from datetime import datetime
from json_storage import JsonStorage


class Password:
    """Build unique password"""

    today = datetime.now()
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    current_date = today.strftime("%Y/%m/%d %H:%M:%S")

    def __init__(self, pass_len, json_storage: JsonStorage):
        self.pass_len = pass_len
        self.new_pass = ''.join(random.choice(self.pass_chars) for _ in range(self.pass_len))
        json_storage.add_to_file(self.new_pass, self.current_date)
