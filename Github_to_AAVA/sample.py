from github import Github
from github import Auth
from dotenv import load_dotenv
load_dotenv()
import os

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REPO_NAME = 'Bala-0078/BankingPortalBackEnd'
BRANCH = 'main'
auth=Auth.Token(ACCESS_TOKEN)


def getting_content():
    g = Github(auth=auth)
    repo = g.get_repo(REPO_NAME)
    contents = repo.get_contents("src/main/", ref=BRANCH)
    print(contents)
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path, ref=BRANCH))
        elif file_content.path.endswith(".java"):
            file_name=file_content.name
            code_content=file_content.decoded_content.decode('utf-8')
            with open(file_name,"w") as f:
                f.write(code_content)


if __name__ == "__main__":
    getting_content()