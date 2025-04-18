from agents.ingest_agent import read_json_files
from agents.extract_agent import extract_emails_from_json
from agents.output_agent import write_emails_to_file

if __name__ == "__main__":
    input_folder = "data"
    output_file = "output/emails.txt"

    json_data = read_json_files(input_folder)
    email_list = extract_emails_from_json(json_data)
    write_emails_to_file(email_list, output_file)

    print(f"✅ Extracted {len(email_list)} email(s) to {output_file}")
