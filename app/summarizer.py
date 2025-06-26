from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# GPT model setup (GPT-4 or GPT-3.5 depending on availability)
llm = ChatOpenAI(model="gpt-4", temperature=0.3)

def generate_meeting_summary(transcript: str):
    """
    Generate TL;DR summary, action items, decisions, and open points from transcript.
    """
    prompt_template = PromptTemplate(
        input_variables=["transcript"],
        template="""
You are an AI meeting assistant. Analyze the following meeting transcript and extract:

1. TL;DR Summary (in 3-5 lines)
2. Action Items with assignee and deadline (if mentioned)
3. Decisions Made
4. Unresolved / Open Questions

Meeting Transcript:
--------------------
{transcript}

Respond in the following format:

## TL;DR Summary
...

## Action Items
- [Assignee] will [task] by [deadline]
...

## Decisions Made
- ...

## Open Points
- ...
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)
    result = chain.run(transcript=transcript)
    return result
 