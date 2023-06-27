# Commit Bot

Commit Bot is a Python script that automates commits in a Git repository. It creates commits at regular intervals, with each commit message containing the current time.

## Requirements

- Python 3
- Git
- GitPython library

## Installation

## Clone the repository to your local machine:

   ``` git clone https://github.com/danalvin/commit-a-bot ```

## Install the required dependencies:

``` pip install GitPython ```

## Usage
Set up your Git repository and ensure it is initialized.

Open the commit_bot.py script in a text editor.

Modify the ``` repo_path ``` variable to specify the path to your local Git repository.

Save the changes to commit_bot.py.

Run the script using the following command:

``` python commit_bot.py ```


The script will create six commits per day, with each commit message containing the current time.

To stop the script, press Ctrl + C.

## Customization
To adjust the number of commits or the time interval between commits, modify the loop in the commit_bot.py script.

Customize the commit messages or the contents of the files created by modifying the create_commit() function in the script.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.