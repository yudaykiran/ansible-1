import subprocess

# Hard-Coded for your repo (ToDo: get from remote?)
GITHUB_USER="chandan.kr404@gmail.com"
REPO="ansible"

print("Starting pre-commit hook...")

BRANCH=subprocess.check_output(["git",
                                "rev-parse",
                                "--abbrev-ref",
                                "HEAD"]).strip()

# String with hard-coded values
# See Embedding Status Images[3] for alternate formats (private repos, svg, etc)

#  [![Build Status](https://travis-ci.org/
#  joegattnet/joegattnet_v3.png?
#  branch=staging)][travis]

# Output String with Variable substitution
travis="[![Build Status](https://travis-ci.org/" \
       "{GITHUB_USER}/{REPO}.png?" \
       "branch={BRANCH})][travis]\n".format(BRANCH=BRANCH,
                                            GITHUB_USER=GITHUB_USER,
                                            REPO=REPO)

sentinel_str="[![Build Status]"

readmelines=open("README.md").readlines()
with open("README.md", "w") as fh:
    for aline in readmelines:
        if sentinel_str in aline and travis != aline:
            print "Replacing:\n\t{aline}\nwith:\n\t{travis}".format(
                   aline=aline,
                   travis=travis)
            fh.write(travis)
        else:
            fh.write(aline)

subprocess.check_output(["git", "add", "README.md" ])

print("pre-commit hook complete.")