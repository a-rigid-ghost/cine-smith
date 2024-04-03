from openai import OpenAI

def get_dialogue(idea_prompt: str):
    client = OpenAI()
    final_prompt = f"Create an enumerated list of {idea_prompt} and write a few short sentences for each of them explaining why"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": final_prompt}
        ]
    )
    return completion.choices[0].message.content
