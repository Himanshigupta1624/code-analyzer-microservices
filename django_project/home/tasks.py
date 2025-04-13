# tasks.py
from celery import shared_task
from home.utils.github import analyze_pr

@shared_task
def analyse_repo_task(repo_url, pr_number, github_token=None):
    # # Ensure github_token is either None or a string
    # if github_token == {} or (isinstance(github_token, dict) and not github_token):
    #     github_token = None
    # elif isinstance(github_token, dict) and github_token:
    #     # If it's a non-empty dict, try to extract a string token
    #     if 'token' in github_token:
    #         github_token = github_token['token']
    #     else:
    #         # Try to get the first value as a fallback
    #         github_token = next(iter(github_token.values()), None)
    
    # # Now github_token should be None or a string
    # result = analyze_pr(repo_url, pr_number, github_token)
    # return result
    result=analyze_pr(repo_url,pr_number,github_token)
    return result

