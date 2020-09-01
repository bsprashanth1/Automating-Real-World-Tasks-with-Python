#!/usr/bin/env python3

import os
import socket
import shutil
import psutil
import emails


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usuage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_memory_usuage():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500

def check_cpu_usuage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def send_email(subject):
    sender = "automation@example.com"
    recipient = "student-03-20dba3e40b55@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_mail(sender, recipient, subject, body, '')
    emails.send_email(message)


if not check_cpu_usuage():
    subject = "Error - CPU usage is over 80%"
    print(subject)
    send_email(subject)

if not check_memory_usuage():
    subject = "Error - Available disk space is less than 20%"
    print(subject)
    send_email(subject)

if not check_disk_usuage('/'):
    subject = "Error - Available memory is less than 500MB"
    print(subject)
    send_email(subject)

if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    print(subject)
    send_email(subject)


