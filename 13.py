from datetime import datetime, timedelta

class Case:
    def __init__(self, name, created_task, end_task=None):
        self.name = name
        self.created_task = self.parse_datetime(created_task)
        self.end_task = self.parse_datetime(end_task) if end_task else None

    def parse_datetime(self, datetime_in_string):
        if datetime_in_string:
            return datetime.fromisoformat(datetime_in_string)
        return None

    def retrieve_seconds(self):
        if self.end_task is not None:
            duration = self.end_task - self.created_task
            return int(duration.total_seconds())
        else:
            # If end_task is None, the task is still ongoing
            return None


first_case_data = {
    'name': 'first_case',
    'created_task': '2021-10-26T19:48:12+00:00',
    'end_task': None
}

second_case_data = {
    'name': 'second_case',
    'created_task': '2021-09-26T19:48:12+00:00',
    'end_task': '2021-10-26T19:48:12+00:00'
}

first_case = Case(**first_case_data)
second_case = Case(**second_case_data)

seconds_first_case = first_case.retrieve_seconds()
seconds_second_case = second_case.retrieve_seconds()

print(f"Seconds for {first_case.name}: {seconds_first_case}")
print(f"Seconds for {second_case.name}: {seconds_second_case}")
