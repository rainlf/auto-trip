from task.task_executor import TaskExecutor


module = 'captain'
# task: TaskExecutor = TaskExecutor(module, 'task_publish')
task: TaskExecutor = TaskExecutor(module, 'task_publish_b')
task.print_task_list()
# task.execute()
#
# module = 'qconfig'
# task: TaskExecutor = TaskExecutor(module, 'publish')
# task.execute()

