import os

def email_draft_preview():
    """
    Preview the email draft if it exists.
    """
    print("\n===== EMAIL DRAFT PREVIEW =====\n")
    
    draft_path = "output/email_draft.txt"
    if os.path.exists(draft_path):
            with open(draft_path, "r", encoding="utf-8") as f:
                draft_content = f.read()
            print("\n===== EMAIL DRAFT PREVIEW =====\n")
            print(draft_content)
            print("\n===============================\n")
    else:
            print(" No draft file found yet.")
    return draft_content