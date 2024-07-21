# https://docs.multion.ai
# Make sure that the MultiOn Chrome Extension is installed and enabled (for more details, see here).

import os
from multion.client import MultiOn

class MultiOnUtils:
    def __init__(self):
        self.multion_api_key = os.environ.get("MULTION_API_KEY") # Get your API key from https://app.multion.ai/api-keys
        if not self.multion_api_key:
            raise ValueError("MULTION_API_KEY is not set in .env variables")
    def visit_event_website(self):
        client = MultiOn(api_key=self.multion_api_key)
        # client = MultiOn(api_key=multion_api_key,agentops_api_key=os.environ.get("AGENTOPS_API_KEY"))

        create_response = client.sessions.create(
            url=os.environ.get("EVENT_WEBSITE"),
            local=True
        )
        session_id = create_response.session_id

        return session_id

    def scrap_website(self, session_id):
        client = MultiOn(api_key=self.multion_api_key)
        # client = MultiOn(api_key=multion_api_key,agentops_api_key=os.environ.get("AGENTOPS_API_KEY"))

        retrieve_response = client.retrieve(
            url=os.environ.get("EVENT_WEBSITE"),
            cmd="For the event, get its: name, date, venue, judges, sponsors, prizes",
            fields=["website_url", "name", "date", "venue", "judges", "sponsors", "prizes"]
        )

        data = retrieve_response.data
        print(data)
        return data