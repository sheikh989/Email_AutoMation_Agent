import sys
from automation.crew import AutomationAgent
from datetime import datetime
import os



def run():
    """
    Run the crew.
    """
    inputs = {

        'query': "send email to sheikhupdesk@gmail.com and tell him about the bruj khalifa",
        'attach_file_path':None,#'IMG_20230806_124823_x16.jpg',  # Optional file path for attachment
        'csv_file':None,#'S:\AffyCloud\Crew AI\Automation_agent\Book1.csv',  # Optional CSV file path for email
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    os.environ["CREW_QUERY"] = inputs["query"]
    result=AutomationAgent().crew().kickoff(inputs=inputs)

    return print(result.rew)
    