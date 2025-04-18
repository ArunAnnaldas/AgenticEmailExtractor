def write_emails_to_file(email_list, output_file):
    with open(output_file, 'w') as f:
        for email in email_list:
            f.write(email + "\n")
