Implement a function `execute_task` to deserialize and execute custom data processing tasks submitted by users to a cloud-based service. Tasks are defined by serialized objects specifying the task type and parameters. 

-----Examples-----
Input:
serialized_task = "type: data_analysis\ndata_id: 42"
execute_task(serialized_task)
Output:
'Executed task: data_analysis'
