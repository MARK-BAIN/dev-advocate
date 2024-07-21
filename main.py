from dotenv import load_dotenv
from src import multion

load_dotenv()

def main():
    multionscrapper = multion.MultiOnUtils()
    session_id = multionscrapper.visit_event_website()
    multionscrapper.scrap_website(session_id)

if __name__ == "__main__":
    main()