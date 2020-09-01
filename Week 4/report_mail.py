#!/usr/bin/env python3

import os
import reports
import emails


if __name__ == '__main__':
    path = "supplier-data/descriptions"
    paragraph = ""
    for file in os.listdir(path):
        with open(path + "/" +file, 'r', encoding='utf-8') as text:
            test_list = text.readlines()
            paragraph += "name: "+test_list[0] + "<br/>weight: " + test_list[1] +"<br/>"
        paragraph += "<br/>"

    # reports.generate_report("/tmp/processed.pdf","Processed Update on ",paragraph)
    reports.generate_report("processed.pdf","Processed Update on ",paragraph)

    sender = "automation@example.com"
    recipient = "student-03-20dba3e40b55@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    message = emails.generate_mail(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)