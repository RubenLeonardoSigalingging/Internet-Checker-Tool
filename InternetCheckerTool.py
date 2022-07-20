#!/usr/bin/env python3


import socket
import requests
from os import system
system("clear")


def Internet_Checker_Tool(Created_By="Ruben Leonardo Sigalingging"):
	if socket.gethostbyname(socket.gethostname())=="127.0.0.1":
		print(f"No Internet Network Connection!")
		print(f"Your IP Address Is: {socket.gethostbyname(socket.gethostname())}\n")
	else:
		print(f"Connected To {requests.get('https://api.ipify.org/').text}\n")
Internet_Checker_Tool()