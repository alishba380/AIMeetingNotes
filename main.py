from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()


class MeetingNotes(BaseModel):
    notes: str

@app.post("/summarise")
def summarise_meeting(data: MeetingNotes):
    
    prompt = f"""
    You are an assistant that summarises meeting notes.
    Given the raw meeting notes below, return:
    1. A short clean summary (3-4 sentences). 
    2. Create clean and straightforward bullet point lists and highlight all the important points discussed in the meeting notes
    
    
    Example input: 
    "john said we need to fix the login bug asap, sara will handle the frontend changes by friday, 
    ahmed needs to update the database schema, we also talked about the new feature but didnt decide anything yet,
    next meeting is monday"

    Example Output: 
    "summary": "The team discussed the login bug and decided to prioritize fixing it ASAP. Sara will handle the frontend changes by Friday, while Ahmed will update the database schema. A discussion on a new feature was also initiated, but no decisions were made yet.",
    1. John is supossed to fix the login bug. Deadline is ASAP,
    2. Sara is supossed to fix frontend. Deadline is Friday,
    3. Ahmed is supossed to update database schema. Deadline is not specified,
    4. Next meeting is on Monday
  
    Meeting Notes:
    {data.notes}
    """
    
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {"result": response['message']['content']}