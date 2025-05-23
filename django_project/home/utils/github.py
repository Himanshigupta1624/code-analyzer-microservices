import requests
import base64
from urllib.parse import urlparse
import uuid
from .ai_agent import analyze_code_with_llm

def get_owner_and_repo(url):
    passed_url = urlparse(url)
    path_parts = passed_url.path.strip("/").split("/")
    if len(path_parts) >= 2:
        owner, repo = path_parts[0], path_parts[1]
        return owner, repo
    return None, None

def fetch_pr_files(repo_url, pr_number, github_token=None):
    owner, repo = get_owner_and_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {}
    
    # Check if github_token is a dictionary and extract the actual token
    if github_token and isinstance(github_token, str):
        headers["Authorization"] = f"token {github_token}"
    
    print(f"Headers for PR files: {headers}")
    response = requests.get(url, headers=headers)
    
    response.raise_for_status()
    return response.json()

def fetch_file_content(repo_url, file_path, github_token=None):
    owner, repo = get_owner_and_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {}
    if github_token and isinstance(github_token, str):
        headers["Authorization"] = f"token {github_token}"
    
    print(f"Headers for PR files: {headers}")
    response = requests.get(url, headers=headers)
    
    response.raise_for_status()
    content = response.json()
    return base64.b64decode(content['content']).decode()

def analyze_pr(repo_url, pr_number, github_token=None):
    task_id = str(uuid.uuid4())
    try:
        pr_files = fetch_pr_files(repo_url, pr_number, github_token)
        print(f"Number of PR files: {len(pr_files)}") 
        analysis_results = []
        for file in pr_files:
            file_name = file['filename']
            print(f"Processing file: {file_name}")
            raw_content = fetch_file_content(repo_url, file_name, github_token)
            
            file_analysis_results = analyze_code_with_llm(raw_content, file_name)
            analysis_results.append(file_analysis_results)
        print(f"Analysis complete, {len(analysis_results)} results")    
            
        return {
            "task_id": task_id,
            "results": analysis_results
        }
    except Exception as e:
        print(f"Error analyzing PR: {e}")
        return {
            "task_id": task_id,
            "error": str(e),
            "results": []
        }