# https://docs.multion.ai
# Make sure that the MultiOn Chrome Extension is installed and enabled (for more details, see here).

import os
from multion.client import MultiOn
from mem0 import Memory

class MultiOnUtils:
    def __init__(self):
        self.multion_api_key = os.environ.get("MULTION_API_KEY") # Get your API key from https://app.multion.ai/api-keys
        self.agentops_api_key = os.environ.get("AGENTOPS_API_KEY")  # Get your API key from https://app.agentops.ai/settings/projects
        if not self.multion_api_key:
            raise ValueError("MULTION_API_KEY is not set in .env variables")

        self.scrapper_fields = ["url", "object", "name", "date", "venue", "people", "companies", "technologies"]

    def visit_event_website(self):
        client = MultiOn(api_key=self.multion_api_key, agentops_api_key=self.agentops_api_key)

        create_response = client.sessions.create(
            url= "https://lu.ma/ai-agents-2.0?tk=5epBFf",
            local=True
        )
        session_id = create_response.session_id

        return session_id

    def scrap_website(self, session_id):
        client = MultiOn(api_key=self.multion_api_key, agentops_api_key=self.agentops_api_key)

        retrieve_response = client.retrieve(
            url= "https://lu.ma/ai-agents-2.0?tk=5epBFf",
            cmd="""
                For the page, get its: 
                    - url,
                    - type of object it is like article/event/course, 
                    - name,
                    - date,
                    - venue (if applicable), 
                    - people,
                    - companies, 
                    - Major technologies/problems
            """,
            fields=self.scrapper_fields
        )

        data = retrieve_response.data
        # print("MEM0_1")
        self.memorize_user_data(data)

        return data
    
    def scrap_linkedin(self):
        client = MultiOn(api_key=self.multion_api_key, agentops_api_key=self.agentops_api_key)
        create_response = client.sessions.create(
        url="https://linkedin.com",
        local=True
        )

        session_id = create_response.session_id
        status = "CONTINUE"

        linkedin_url = "https://www.linkedin.com/in/alex-reibman-67951589/"

        while status == "CONTINUE":
            step_response = client.sessions.step(
                session_id=session_id,
                cmd=f"open {linkedin_url}"
            )
            status = step_response.status

        retrieve_response = client.retrieve(
            session_id=session_id,
            cmd="Get name, headline, location, current position, profile URL, and image URL.",
            fields=["name", "headline", "location", "current_position", "profile_url", "image_url"],
            scroll_to_bottom=True,
            render_js=True
        )

        print(retrieve_response.data[0])
        data = retrieve_response.data[0]

        return data

    def scrap_github(self):
        client = MultiOn(api_key=self.multion_api_key, agentops_api_key=self.agentops_api_key)
        create_response = client.sessions.create(
            url="https://github.com/areibman",
            local=True
        )

        session_id = create_response.session_id
        retrieve_response = client.retrieve(
            session_id=session_id,
            cmd="Get name, location, number of repositories, count of contributions in the last year, followers and following count.",
            fields=["name", "location", "pulbic_repositories", "last_year_contributions_count", "github_followers_count", "github_following_count"],
            scroll_to_bottom=True,
            render_js=True
        )

        print(retrieve_response.data)
        data = retrieve_response.data

        return data

    def memorize_user_data(self, data):
        USER_DATA = f"""
            I visited that page {data[0]['url']} of {data[0]['object']},
            And I want to know more about these people {data[0]['people']},
            I'd love to connect more with these companies {data[0]['companies']},
            And I'd love to work on problems/technologies {data[0]['technologies']},
            It's in {data[0]['venue']} on {data[0]['date']},
        """
        # print("MEM0_2")
        m = Memory()
        memory = m.add(USER_DATA, user_id="rob", metadata={"category": "career interests"})
        print(memory)
        # print("MEM0_3")

        all_memories = m.get_all()
        print(all_memories)
