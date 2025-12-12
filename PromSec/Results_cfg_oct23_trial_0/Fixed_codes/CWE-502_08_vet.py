import os

def execute_task(serialized_task):
    task_info = {}
    for line in serialized_task.split('\n'):
        key, value = line.split(': ')
        task_info[key] = value

    if task_info['type'] == 'data_analysis':
        data_id = task_info['data_id']
        # Execute data analysis task with data_id
        return 'Executed task: data_analysis'

# Example
serialized_task = "type: data_analysis\ndata_id: 42"
execute_task(serialized_task)