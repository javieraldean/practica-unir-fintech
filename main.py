"""
License: Apache
Organization: UNIR
"""

import os
import sys
import subprocess

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = True


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Can't order {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))

def process_git_log(show_unique=False):
    try:
        # Simulates getting the Git log
        result = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True, check=True)
        log_lines = result.stdout.strip().split('\n')
        words = []
        for line in log_lines:
            words.extend(line.split())

        if show_unique:
            unique_words = sorted(list(set(words)))
            print("\nUnique words in the log:")
            for word in unique_words:
                print(word)
        else:
            print("\nAll words in the log:")
            for word in words:
                print(word)

    except subprocess.CalledProcessError as e:
        print(f"Error executing the git log command: {e}")
    except FileNotFoundError:
        print("The 'git' command was not found. Ensure Git is installed and in your PATH.")



if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order = DEFAULT_ORDER
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order = sys.argv[3].lower() == "asc"
    else:
        print("The file must be specified as the first argument.")
        print("The second argument indicates whether you want to remove duplicates.")
        print("The third argument indicates the order. (asc o desc)")
        sys.exit(1)

    print(f"The words in the file will be read {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, order))

    show_unique = False
    if "--unique" in sys.argv:
        show_unique = True
        # Remove the --unique flag from the arguments to avoid interfering with other commands
        sys.argv.remove("--unique")

    process_git_log(show_unique)

    if len(sys.argv) > 1:
        command = ['git'] + sys.argv[1:]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print("\nOutput of the Git command:", result.stdout)
            if result.stderr:
                print("Git command errors:", result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the Git command '{' '.join(command)}': {e}")
        except FileNotFoundError:
            print("The 'git' command was not found.")