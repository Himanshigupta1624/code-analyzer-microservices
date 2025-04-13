from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import analyse_repo_task
from celery.result import AsyncResult

@api_view(['POST'])
def start_task(request):
    data=request.data
    repo_url=data.get('repo_url')
    pr_number=data.get('pr_number')
    github_token=data.get('github_token')
    task=analyse_repo_task.delay(repo_url,pr_number,github_token)
    print(f"TASK ID: {task.id}")
    return Response({"task_id":task.id,
                     "status":"Task Started"})
    
    
@api_view(['GET'])
def task_status_view(request,task_id):
    try:
        result=AsyncResult(task_id)
        response={
            "task_id":task_id,
            "status":result.state
        }
        if result.ready():
            response["result"] = result.get()
        return Response(response)
    except Exception as e:
        return Response({"error": str(e), "detail": "Task not found"}, status=404)
        
