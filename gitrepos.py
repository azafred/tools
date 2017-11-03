#!/usr/bin/env python
# This script will clone or pull every repo you have on your github account
# which is either yours (public and private) or forked.
# If the repo is a fork, it will store it in a 'forks' subdirectory
# Author: Fred Vassard <azafred@gmail.com>

import pygithub3
import os
import shlex
from subprocess import check_output

gh = None
token = "xxxxxxxxxxxxxxxxxxxxxx"  # Create a token on your github account
users = ['azafred', 'comapny']  # your username and/or organization name or other things you want to track
gh_user = 'azafred'  # Your username

def gather_repos(ghusers, no_forks=False):
    gh = pygithub3.Github(user=gh_user, token=token)
    repos = {}
    for user in ghusers:
        ghrepo = gh.repos.list(user=user).all()
        for r in ghrepo:
            repos[r.name] = {
                'name': r.name, 'org': user, 'fork': r.fork,
                'ssh_url': r.ssh_url}
    return repos


def gitpull(repo):
    original_dir = os.getcwd()
    if repo['fork']:
        repo_dir = 'forks/{}'.format(repo['name'])
    else:
        repo_dir = repo['name']
    os.chdir(repo_dir)
    cmd = "git pull --rebase"
    try:
        rebase = check_output(shlex.split(cmd))
        print(rebase)
    except Exception as e:
        print(e)
    os.chdir(original_dir)


def clone_repo(repo, target_dir='./'):
    original_dir = os.getcwd()
    os.chdir(target_dir)
    cmd = "git clone {}".format(repo['ssh_url'])
    try:
        clone = check_output(shlex.split(cmd))
        print(clone)
    except:
        print("looks like {} is already cloned").format(repo['name'])
        print("Doing a git pull instead:")
        os.chdir(original_dir)
        gitpull(repo)
    os.chdir(original_dir)


def create_forks_dir():
    try:
        if not os.path.exists('forks'):
            os.mkdir('forks')
        return True
    except:
        return False


def main():
    repos = gather_repos(users, no_forks=False)
    create_forks_dir()
    for repo in repos.values():
        if repo['fork']:
            print("{} forks/{}").format(repo['ssh_url'], repo['name'])
            clone_repo(repo, target_dir='forks')
        else:
            print("{} {}").format(repo['ssh_url'], repo['name'])
            clone_repo(repo)


if __name__ == "__main__":

    main()

