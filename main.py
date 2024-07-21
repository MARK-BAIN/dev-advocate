from src import multion
def main():
    session_id = multion.visit_event_website()
    multion.scrap_website(session_id)

if __name__ == "__main__":
    main()