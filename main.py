import os
from instagrapi import Client

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)

# recent 10 group chats fetch karega
threads = cl.direct_threads(10)

print("\n👉 Your Recent Group Chats:")
for t in threads:
    print("🆔", t.id, "| 📌", t.thread_title)

THREAD_ID = input("\nThread ID daalo: ")
NEW_NAME = input("Naya GC name daalo: ")

cl.direct_thread_rename(THREAD_ID, NEW_NAME)
print("✅ GC name changed successfully to:", NEW_NAME)
