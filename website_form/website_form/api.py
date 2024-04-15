import frappe
from frappe.sessions import get_csrf_token
csrf_token = get_csrf_token()


@frappe.whitelist(allow_guest=True)
def get_all_inputs(your_name = "", your_email = "", your_subject = "", your_message = ""):
    try:

        # Create a new document and save it in the database
        data = frappe.new_doc("webcitform")
        data.your_name = your_name
        data.your_email = your_email
        data.your_subject = your_subject
        data.your_message = your_message
        
       

      #  my name

        if your_name is not None and your_email is not None and your_subject is not None and your_message is not None:
          pass
        data.insert()
        frappe.db.commit()
        
        return {"message": "Form submitted successfully"}
    except Exception as e: 
        frappe.log_error(f"Error while processing form submission: {str(e)}", "get_all_inputs")
        return {"message": "An error occurred while processing the form submission. Please try again later."}








