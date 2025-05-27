#!/usr/bin/env python3
"""
GitHub PR Creator

This script prompts for agent metadata and creates a pull request
directly on GitHub with the metadata in the PR description.
"""

import os
import sys
import logging
import datetime
import getpass
import argparse
import tempfile
import shutil
import json
import re
import uuid
from typing import Dict, Optional

# UUID pattern constant
PARTY_ID_REGEXP = r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"

# Third party imports
try:
    import git
    from github import Github, GithubException
except ImportError:
    print("Required packages not found. Please install with:")
    print("pip install GitPython PyGithub")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("pr_creator")

PR_INFO_FILE = "pr_publish_details.json"


def load_pr_info() -> Dict[str, Dict[str, str]]:
    if os.path.exists(PR_INFO_FILE):
        try:
            with open(PR_INFO_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {PR_INFO_FILE}. Returning empty data.")
            return {}
    return {}


def save_pr_info(all_info: Dict[str, Dict[str, str]]):
    try:
        with open(PR_INFO_FILE, 'w') as f:
            json.dump(all_info, f, indent=4)
    except IOError as e:
        logger.error(f"Error writing PR info to {PR_INFO_FILE}: {e}")


def store_pr_details(agent_name_slug: str, branch_name: str, repo_url: str, pr_url: str):
    all_info = load_pr_info()
    all_info[agent_name_slug] = {
        "branch_name": branch_name,
        "repo_url": repo_url,
        "pr_url": pr_url,
        "last_updated_script": datetime.datetime.now().isoformat()
    }
    save_pr_info(all_info)
    logger.info(f"Stored PR details for agent '{agent_name_slug}' in {PR_INFO_FILE}")


def get_stored_pr_details(agent_name_slug: str) -> Optional[Dict[str, str]]:
    all_info = load_pr_info()
    details = all_info.get(agent_name_slug)
    if details:
        logger.info(f"Retrieved stored PR details for agent '{agent_name_slug}'")
        return details
    else:
        logger.warning(f"No stored PR details found for agent '{agent_name_slug}'")
        return None


def get_user_input(prompt: str, required: bool = True, default: Optional[str] = None) -> str:
    try:
        if default:
            full_prompt = f"{prompt} [{default}]: "
        else:
            full_prompt = f"{prompt}: "
        while True:
            user_input = input(full_prompt).strip()
            if not user_input and default:
                return default
            elif not user_input and required:
                print("This field is required. Please try again.")
            else:
                return user_input
    except (EOFError, KeyboardInterrupt):
        if default:
            return default
        # Sample values based on prompt
        if "name" in prompt.lower():
            return "Sample Agent"
        else:
            return "sample_value"


def get_password_input(prompt: str, required: bool = True) -> str:
    try:
        while True:
            password = getpass.getpass(f"{prompt}: ")
            if not password and required:
                print("This field is required. Please try again.")
            else:
                return password
    except (EOFError, KeyboardInterrupt):
        print("[Using sample GitHub token for demonstration]")
        return "sample_github_token"


def generate_valid_party_id() -> str:
    """Generate a valid party_id that matches the required pattern."""
    return str(uuid.uuid4())


def create_pull_request(token: str, repo_url: str, agent_name: str, agent_folder_name: str,
                        base_branch: str = "main",
                        agent_description_from_config: str = "N/A",
                        contributors_str: str = "N/A",
                        existing_branch_name: Optional[str] = None,
                        existing_pr_url: Optional[str] = None) -> str:
    try:
        if "github.com" in repo_url:
            if repo_url.startswith("git@"):
                parts = repo_url.split(":")
                owner_repo = parts[1].replace(".git", "")
            else:
                parts = repo_url.split("github.com/")
                owner_repo = parts[1].replace(".git", "")
            owner_name, repo_name = owner_repo.split("/")
        else:
            raise ValueError(f"Invalid GitHub repository URL: {repo_url}")

        g = Github(token)
        github_repo = g.get_repo(f"{owner_name}/{repo_name}")

        is_update = bool(existing_branch_name)
        branch_to_operate_on: str

        if is_update:
            if not existing_branch_name:
                raise ValueError("existing_branch_name must be provided for an update.")
            branch_to_operate_on = existing_branch_name
            logger.info(f"Updating existing branch: {branch_to_operate_on}")
        else:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            branch_to_operate_on = f"add-{agent_name.lower().replace(' ', '-')}-{timestamp}"
            logger.info(f"Creating new branch for PR: {branch_to_operate_on}")

        with tempfile.TemporaryDirectory() as temp_dir:
            if repo_url.startswith("https://"):
                auth_url = repo_url.replace("https://", f"https://{token}@")
            else:
                auth_url = repo_url

            try:
                logger.info(f"Cloning repository {repo_url} (branch {base_branch}) to {temp_dir}")
                repo = git.Repo.clone_from(auth_url, temp_dir, branch=base_branch)
                logger.info(f"Successfully cloned repository from base branch {base_branch}")

                if is_update:
                    try:
                        origin = repo.remote(name='origin')
                        origin.fetch()
                        remote_branch_ref = None
                        for ref in origin.refs:
                            if ref.name == f"origin/{branch_to_operate_on}":
                                remote_branch_ref = ref
                                break
                        if not remote_branch_ref:
                            logger.error(f"Remote branch origin/{branch_to_operate_on} does not exist. Cannot update.")
                            raise Exception(f"Remote branch origin/{branch_to_operate_on} not found. Cannot update.")
                        if branch_to_operate_on in repo.heads:
                            logger.info(f"Checking out existing local branch: {branch_to_operate_on}")
                            repo.git.checkout(branch_to_operate_on)
                        else:
                            logger.info(
                                f"Creating local branch {branch_to_operate_on} tracking origin/{branch_to_operate_on}")
                            repo.create_head(branch_to_operate_on, remote_branch_ref).set_tracking_branch(
                                remote_branch_ref).checkout()
                        logger.info(f"Successfully checked out branch {branch_to_operate_on} for update.")
                    except git.GitCommandError as e_checkout:
                        logger.error(
                            f"Failed to checkout or set up branch {branch_to_operate_on} for update: {e_checkout}")
                        raise Exception(f"Failed to prepare branch {branch_to_operate_on} for update: {e_checkout}")
                else:
                    logger.info(f"Creating and checking out new branch: {branch_to_operate_on}")
                    new_branch_obj = repo.create_head(branch_to_operate_on)
                    repo.git.checkout(branch_to_operate_on)

                pr_body_checklist_checked = """## Checklist

- [x] I have performed a self-review of my code.
- [x] I have commented on my code, particularly in hard-to-understand areas.
- [x] I have not hardcoded API keys and other sensitive information in the code.
- [x] I followed the documentation and created all the necessary folders and files, including a folder with a unique name to house the files.
- [x] I have updated `party_id`, `port`, `agent_name`, `description`, etc., in `config.json`.
- [x] I have updated the folder path in the `Dockerfile` and also updated the port used in `main.py` within the `Dockerfile`.
- [x] I have updated the system prompt for the Agent/Team and edited its name.
- [x] I have run `main.py` locally and confirmed code is working as expected, referring to the documentation throughout the process."""

                pr_body = (
                    f"## Agent Description\n\n{agent_description_from_config}\n\n"
                    f"## Who all contributed to this PR?\n\n{contributors_str}\n\n"
                    f"{pr_body_checklist_checked}"
                )

                repo_agents_base_dir = "agents"
                repo_agent_target_dir = os.path.join(repo_agents_base_dir, agent_folder_name)
                full_target_dir_in_clone = os.path.join(temp_dir, repo_agent_target_dir)
                os.makedirs(full_target_dir_in_clone, exist_ok=True)
                logger.info(f"Ensured agent target directory exists in clone: {full_target_dir_in_clone}")

                publish_list_file_path = os.path.abspath("publish_list.txt")
                current_adfile_being_processed = None

                with open(publish_list_file_path, 'r') as push_list_file:
                    count = 0
                    for line in push_list_file:
                        source_file_relative_to_script = line.strip()
                        if not source_file_relative_to_script:
                            continue
                        count += 1
                        current_adfile_being_processed = source_file_relative_to_script
                        logger.info(f"Processing file from list: {source_file_relative_to_script}")
                        source_file_abs_path = os.path.abspath(source_file_relative_to_script)
                        if source_file_relative_to_script.startswith(agent_folder_name + os.sep):
                            file_path_within_agent_folder = source_file_relative_to_script[
                                                            len(agent_folder_name) + len(os.sep):]
                        else:
                            logger.warning(
                                f"File '{source_file_relative_to_script}' does not seem to be inside the agent folder '{agent_folder_name}'. Using its basename as fallback.")
                            file_path_within_agent_folder = os.path.basename(source_file_relative_to_script)
                        dest_file_in_repo_abs_path = os.path.join(temp_dir, repo_agent_target_dir,
                                                                  file_path_within_agent_folder)
                        if not os.path.exists(source_file_abs_path):
                            logger.error(
                                f"Source file {source_file_abs_path} (from entry '{source_file_relative_to_script}') not found. Skipping.")
                            continue
                        os.makedirs(os.path.dirname(dest_file_in_repo_abs_path), exist_ok=True)
                        logger.info(f"Copying {source_file_abs_path} to {dest_file_in_repo_abs_path}")
                        shutil.copy(source_file_abs_path, dest_file_in_repo_abs_path)
                        git_add_path = os.path.join(repo_agent_target_dir, file_path_within_agent_folder)
                        repo.git.add(git_add_path)
                        logger.info(f"Added {git_add_path} to git staging area.")

                logger.info(f"Processed {count} file entries from {os.path.basename(publish_list_file_path)}")

                commit_message: str
                if is_update:
                    commit_message = f"Update metadata and files for {agent_name} agent"
                else:
                    commit_message = f"Add metadata for {agent_name} application"
                repo.git.commit('-m', commit_message)
                logger.info(f"Committed changes: {commit_message}")

                logger.info(f"Pushing branch {branch_to_operate_on} to origin")
                repo.git.push('--set-upstream', '--force', 'origin', branch_to_operate_on)
                logger.info(f"Successfully pushed branch {branch_to_operate_on} to GitHub")

                if is_update:
                    logger.info(f"Branch {branch_to_operate_on} updated successfully for agent {agent_name}.")
                    if existing_pr_url:
                        return existing_pr_url
                    else:
                        return f"Branch {branch_to_operate_on} updated, but no existing PR URL was available."
                else:
                    pr_title = f"Add metadata for {agent_name} application"
                    pr = github_repo.create_pull(
                        title=pr_title,
                        body=pr_body,
                        head=branch_to_operate_on,
                        base=base_branch
                    )
                    logger.info(f"Created pull request: {pr.html_url}")
                    agent_name_slug = agent_name.lower().replace(" ", "-")
                    store_pr_details(agent_name_slug, branch_to_operate_on, repo_url, pr.html_url)
                    return pr.html_url
            except git.GitCommandError as e:
                logger.error(f"Git operation failed: {e}")
                raise Exception(f"Git operation failed: {e}")
            except IOError as e:
                error_message = f"IOError processing file"
                if current_adfile_being_processed:
                    error_message += f" '{current_adfile_being_processed}'"
                error_message += f": {e}"
                logger.error(error_message)
                raise Exception(error_message)
    except GithubException as e:
        logger.error(f"Failed to create pull request: {e}")
        raise


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Create a pull request on GitHub with application metadata"
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Run in non-interactive mode with sample values (for testing)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    print("\n========== GitHub PR Creator ==========")
    print("This script will create a GitHub pull request with application metadata.")
    print("The script will clone the repository, create a branch, and add all files in publish_list.txt.\n")
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    action_choice = ""
    agent_name = ""
    github_token = ""

    if args.non_interactive:
        print("[Running in non-interactive mode with sample values]")
        action_choice = "publish"
        agent_name = "Sample Agent"
        github_token = os.environ.get("GITHUB_TOKEN", "sample_github_token")
    else:
        existing_branch_name_for_update: Optional[str] = None
        existing_pr_url_for_update: Optional[str] = None
        try:
            while True:
                raw_choice = get_user_input(
                    "What would you like to do?\n"
                    "1. Publish a new agent\n"
                    "2. Update an existing agent PR\n"
                    "3. Exit\n"
                    "Enter your choice: ",
                    required=True
                ).lower()
                if raw_choice == "1":
                    action_choice = "publish"
                    logger.info(f"User selected action: {action_choice} (1)")
                    break
                elif raw_choice == "2":
                    action_choice = "update"
                    logger.info(f"User selected action: {action_choice} (2)")
                    break
                elif raw_choice == "3":
                    print("\n\n[User interruption. Exiting.]")
                    sys.exit(1)
                else:
                    print("Invalid choice.")
                    continue

            print("\n--- Agent Information ---")
            agent_name = get_user_input("Enter the agent folder name", required=True)
            agent_name_slug = agent_name.lower().replace(" ", "-")

            if action_choice == "update":
                stored_pr_details = get_stored_pr_details(agent_name_slug)
                if stored_pr_details:
                    print(f"\n--- Existing PR Information for '{agent_name}' ---")
                    print(f"  Branch Name: {stored_pr_details['branch_name']}")
                    print(f"  Repository URL: {stored_pr_details['repo_url']}")
                    print(f"  PR URL: {stored_pr_details['pr_url']}")

                    use_existing = get_user_input(
                        f"Do you want to update the existing branch '{stored_pr_details['branch_name']}'? (y/n)",
                        default="n").lower()
                    if use_existing == 'y':
                        existing_branch_name_for_update = stored_pr_details['branch_name']
                        existing_pr_url_for_update = stored_pr_details['pr_url']
                        print(
                            f"Proceeding to update branch: {existing_branch_name_for_update} in the target repository.")
                    else:
                        print("Proceeding to create a new branch and PR for this agent in the target repository.")
                else:
                    print(
                        f"No existing PR information found for '{agent_name}'. Proceeding to create a new PR in the target repository.")

            logger.info("Base branch is fixed to: main")

            print("\n--- Authentication ---")
            github_token = os.environ.get("GITHUB_TOKEN")
            if not github_token:
                github_token = get_password_input("GitHub token (will not be displayed)")
            else:
                print("Using GitHub token from environment variable GITHUB_TOKEN")
            print("\nProcessing...")

        except (EOFError, KeyboardInterrupt):
            print("\n\n[User interruption. Exiting.]")
            sys.exit(1)

    repo_url = "https://github.com/Lab45-CoreAI/Marketplace-agents.git"
    logger.info(f"Target repository URL is fixed to: {repo_url}")

    if not os.path.exists("./publish_list.txt"):
        print(
            "Missing Publish list file. Create a txt file named publish_list.txt and add files to be pushed to git in each line")
        sys.exit(1)

    config_folder_name = agent_name.lower().replace(" ", "_")
    config_file_path = os.path.join(".", config_folder_name, "config.json")

    if not os.path.exists(config_file_path):
        print(
            f"Missing {config_file_path}. Please ensure the agent's config.json is present in the {config_folder_name} directory.")
        sys.exit(1)

    required_keys = [
        "party_id", "name", "party_type", "description", "tech_stack",
        "category", "service_name", "port", "allow_all_access", "owners",
        "last_updated", "required_file", "required_dataset",
        "prompt1", "prompt2", "prompt3", "api_key"
    ]
    config_data = {}
    try:
        with open(config_file_path, 'r') as f:
            config_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {config_file_path} is not a valid JSON file.")
        sys.exit(1)

    missing_keys = [key for key in required_keys if key not in config_data]
    if missing_keys:
        print(f"Error: Missing keys in {config_file_path}: {', '.join(missing_keys)}")
        sys.exit(1)

    null_or_empty_value_keys = [
        key for key in required_keys
        if
        config_data.get(key) is None or (isinstance(config_data.get(key), str) and config_data.get(key).strip() == "")
    ]
    if null_or_empty_value_keys:
        print(f"Error: Keys with null or empty values in {config_file_path}: {', '.join(null_or_empty_value_keys)}")
        sys.exit(1)

    # Validate party_id format
    party_id = config_data.get("party_id", "")
    if not re.match(PARTY_ID_REGEXP, party_id):
        print(
            f"Error: party_id '{party_id}' in {config_file_path} does not match the required format (12 hexadecimal characters).")
        suggested_party_id = generate_valid_party_id()
        print(f"Suggested valid party_id: {suggested_party_id}")

        print(f"Please update the party_id in {config_file_path} with the suggested value")
        print("Please update the party_id manually to match the required format and try again.")
        sys.exit(1)

    logger.info("publish_list.txt and config.json checks passed.")

    owners_list = config_data.get("owners", [])
    # Validate that each owner has both a non-empty 'name' and 'email'
    invalid_owners = []
    for idx, owner in enumerate(owners_list):
        if not owner.get("name") or not owner.get("email") or str(owner.get("email")).strip() == "":
            invalid_owners.append(idx)
    if invalid_owners:
        print(
            f"Error: Each owner in 'owners' must have both a non-empty 'name' and 'email'. Problem at indices: {invalid_owners}")
        sys.exit(1)

    agent_description_from_config = config_data.get("description", "N/A")
    owners_list = config_data.get("owners", [])
    if owners_list:
        contributors_str = " ".join(
            [f"@{owner.get('name', '').replace(' ', '')}" for owner in owners_list if owner.get('name')])
        if not contributors_str.strip():
            contributors_str = "N/A"
    else:
        contributors_str = "N/A"

    if args.non_interactive:
        checklist_confirmed = True

    if not args.non_interactive:
        confirmation_prompt = (
            f"\n--- PR Confirmation ---\n"
            f"Agent Description (from config.json): {agent_description_from_config}\n"
            f"Contributors (from config.json owners): {contributors_str}\n\n"
            f"The PR will be created with the above information and the following checklist marked as complete:\n"
            f"- [x] I have performed a self-review of my code.\n"
            f"- [x] I have commented on my code, particularly in hard-to-understand areas.\n"
            f"- [x] I have not hardcoded API keys and other sensitive information in the code.\n"
            f"- [x] I followed the documentation and created all the necessary folders and files, including a folder with a unique name to house the files.\n"
            f"- [x] I have updated `party_id`, `port`, `agent_name`, `description`, etc., in `config.json`.\n"
            f"- [x] I have updated the folder path in the `Dockerfile` and also updated the port used in `main.py` within the `Dockerfile`.\n"
            f"- [x] I have updated the system prompt for the Agent/Team and edited its name.\n"
            f"- [x] I have run `main.py` locally and confirmed code is working as expected, referring to the documentation throughout the process.\n\n"
            f"Is this information correct and are you ready to proceed? (y/n)"
        )
        user_confirmation = get_user_input(confirmation_prompt, required=True).lower()
        if user_confirmation != 'y':
            print("PR creation aborted by user. Please update your code or configuration accordingly.")
            sys.exit(0)
        checklist_confirmed = True

    if not checklist_confirmed:
        logger.error("Checklist confirmation failed. Aborting.")
        sys.exit(1)

    try:
        result_url_or_message = create_pull_request(
            github_token,
            repo_url,
            agent_name,
            config_folder_name,
            "main",
            agent_description_from_config,
            contributors_str,
            existing_branch_name=locals().get('existing_branch_name_for_update', None),
            existing_pr_url=locals().get('existing_pr_url_for_update', None)
        )
        if locals().get('existing_branch_name_for_update', None):
            print(
                f"\n✅ Success! Agent '{agent_name}' updated in branch '{locals().get('existing_branch_name_for_update')}'.")
            print(f"   PR URL (if applicable): {result_url_or_message}")
        else:
            print(f"\n✅ Success! Agent Publish Request created: {result_url_or_message}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()