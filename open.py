#!/usr/bin/env python3
import webbrowser
import os

def get_subreddit_names(urls, start, end):
  subreddit_names = []
  for url in urls[start - 1:end]:
    name = url.split('/')[-1].strip()
    subreddit_names.append(name)
  return ', '.join(subreddit_names)

def confirm_and_open(urls, start, end):
  subreddit_names = get_subreddit_names(urls, start, end)
  print(f"You are going to open subreddits: {subreddit_names}")
  confirm = input(f"\nIs that right? :] Continue? (y/n): ")
  if confirm.lower() == 'y':
    for i in range(start - 1, end):
      webbrowser.open_new_tab(urls[i].strip())
      print(f"Opening URL {i + 1}: {urls[i].strip()}")
    print(f"Opened URLs from line {start} to line {end}.")
  else:
    print("Operation cancelled.")

def open_urls(file_path, start, end):
  try:
    with open(file_path, 'r') as file:
      urls = file.readlines()
    if end > len(urls) or end == -1:
      end = len(urls)
    confirm_and_open(urls, start, end)
  except Exception as e:
    print(f"An error occurred: {e}")

def main():
  file_path = 'txt_links.txt' # files name

  try:
    range_input = input("Enter the range of lines to open (format: start,end) or press Enter to open all: ")
    if range_input == '':
      start, end = 1, -1
    else:
      start, end = map(int, range_input.split(','))
      if start < 1 or end < start:
        raise ValueError("Invalid range. Please enter a valid start and end line.")

    open_urls(file_path, start, end)

  except ValueError as e:
    print(f"Invalid input: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()

