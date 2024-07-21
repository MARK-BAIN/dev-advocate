from dotenv import load_dotenv
from src import multion, wordware


load_dotenv()

def main():
    """
        Layer 1/Hardware Layer
        Agent role: Your role is to listen to the human voice inputs, proof-read/correct them and return
        Tools: Friend AI, Datagram

        1. Human user communicates with Friend using Voice control
        2. A webhook of Friend AI is picking up the Voice commands transcribed into text

        Input: Voice control
        Output: text prompt
    """
    # Here goes the Friend AI code
    print("Step 1 completed")

    """
        Layer 2/Private data
        Agent role: Your role is to scrap data from private resources, monitor every step
        Tools: MultiOn, AgentOps, Mem0
        
        1. We receive an intent prompt from a user
        2. We assume a use case where the user wants to learn about people, companies, technologies/problems
        3. We use MultiOn to access private (behind auth) data of the human-in-control user
        4. Multi on Pulls data from intended sources, like Github, LinkedIn, ...
        5. We store pulled data/memories in Mem0

        Input: text prompt
        Output: Mem0 data
    """
    # multionscrapper = multion.MultiOnUtils()
    # session_id = multionscrapper.visit_event_website()
    # retrieve_response = multionscrapper.scrap_website(session_id)
    retrieve_response = [{'website_url': 'https://lu.ma/founders-bay?k=c', 'name': 'AI Agents 2.0: Agents That Work. Hackathon by MultiOn & AgentOps', 'date': 'July 20', 'venue': 'San Francisco, California', 'people': ['Mariane Bekker', 'Div garg', 'Jeremiah Owyang', 'Michelle Gee', 'Alex Reibman', 'Alicia Lin', 'Margarita Groisman', 'Jeremy Nixon', 'Steven Echtman'], 'companies': ['MultiOn', 'AgentOps', 'Founders Bay', 'Arize AI', 'Aiify.io Events', 'AWS', 'Groq', 'Wordware', 'CloudFlare', 'Llama Lounge', 'Llama Index', 'Mem0', 'Founders Institute', 'Anon', 'Based Hardware'], 'technologies': ['AI', 'Agents', 'MultiOn', 'AgentOps', 'AWS', 'Groq', 'Wordware', 'Anon', 'Friend AI Wearables', 'Phoenix Traces', 'Experiments', 'Mem0 API', 'Rabbit R1 AI device', 'SpeedRead', 'DoorDash', 'AI Agents', 'Llama Lounge', 'Silicon Valley Impact', 'Airtags', 'Monitors', 'Electric Scooter', 'Theragun']}]

    print(retrieve_response)
    print("Step 2 completed")

    """
        Layer 3/Agent
        Tools: Mem0, groq
        
        1. We use a custom prompt
        2. Load context to the prompt
        3. Spin up a chatbot
        4. Prompt groq llama3 and execute the prompt. Get JSON
        5. Return the response

        Input: Mem0 data
        Output: JSON
    """
    print("Step 3 completed")

    """
        Layer 4/Wordware
        Input Text prompt
    """
    wordware.main(data=retrieve_response)
    print("Step 4 completed")

    # wordware
if __name__ == "__main__":
    main()