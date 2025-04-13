from groq import Groq
from .prompt import system_prompt
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("GROQ_API_KEY")
def analyze_code_with_llm(file_content,file_name):
    prompt=f"""
    Analyze the following code for:
    - Code style and formatting issues
    - Potential; bugs or error
    - Performance improvements
    - Best Practices
    
    File : {file_name}
    Content : {file_content}
    
    Provide a detailed JSON output with the structure
    {{
        "issues" :[
            {{
                "type" : "<style|bugs|performance|best_practice>",
                "line" : "<line_number>",
                "desription" : "<description>",             
                "suggestion" : "<suggestion>",
            }}
        ]
    }}
    ```json
    """
    client=Groq(
    api_key=key
    )
    try:
        chat_completion= client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content":system_prompt},
                {
                "role":"user" ,
                "content":prompt
                }
            ],
            temperature=1,
            top_p=1
            
            
        )

        result = chat_completion.choices[0].message.content
        
        # print(f"LLM Analysis result for {file_name}: {result}")
        return result
    except Exception as e:
        print(f"Error from LLM API: {e}")
        return {
            "issues": [],
            "error": f"LLM analysis failed: {str(e)}"
        }



