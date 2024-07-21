# https://wordware.notion.site/d603670c4819487fa75185380c885007?v=91206410afab40dc8d92c189284cdb18

import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

def main(data):
    prompt_id = "7c87dade-902c-4519-bf56-9535bb065cb6"
    api_key = os.environ.get("WORDWARE_API_KEY") # Get your API key from https://app.wordware.ai/account/api-keys

    # Describe the prompt (shows just the inputs for now)
    r1 = requests.get(f"https://app.wordware.ai/api/prompt/{prompt_id}/describe",
                      headers={"Authorization": f"Bearer {api_key}"})
    print(json.dumps(r1.json(), indent=4))

    # Execute the prompt
    r = requests.post(f"https://app.wordware.ai/api/prompt/{prompt_id}/run",
                      json={
                          "inputs": {
                              "event_page_data": f"""
                                {data}
                              """,
                              # Image inputs have a different format and require a publicly accessible URL
							  "image": {
                                  "type": "image",
                                  "image_url": "https://i.insider.com/602ee9ced3ad27001837f2ac",
                              },
                          }
                      },
                      headers={"Authorization": f"Bearer {api_key}"},
                      stream=True
                      )

    # Ensure the request was successful
    if r.status_code != 200:
        print("Request failed with status code", r.status_code)
        print(json.dumps(r.json(), indent=4))
    else:
        for line in r.iter_lines():
            if line:
                content = json.loads(line.decode('utf-8'))
                value = content['value']
                # We can print values as they're generated
                if value['type'] == 'generation':
                    if value['state'] == "start":
                        print("\nNEW GENERATION -", value['label'])
                    else:
                        print("\nEND GENERATION -", value['label'])
                elif value['type'] == "chunk":
                    print(value['value'], end="")
                elif value['type'] == "outputs":
                    # Or we can read from the outputs at the end
                    # Currently we include everything by ID and by label - this will likely change in future in a breaking
                    # change but with ample warning
                    print("\nFINAL OUTPUTS:")
                    print(json.dumps(value, indent=4))


if __name__ == '__main__':
    main()