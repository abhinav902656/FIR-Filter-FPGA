# Linux Command Cheat Sheet

> **Project:** FPGA Implementation of Optimized FIR Filter for Signal Processing  
> **Operating System:** Ubuntu 24.04 LTS  
> **Development Environment:** VS Code + Miniconda + Icarus Verilog + GTKWave  
> **Version:** 1.0

---

# About This Handbook

This handbook is a personal reference for Linux commands used during FPGA development.

It includes:

- Linux terminal commands
- File management
- Git and GitHub
- Conda environment management
- Python development
- Verilog simulation
- GTKWave
- VS Code
- Daily workflow
- Troubleshooting

Instead of only listing commands, each section explains:

- Purpose
- Syntax
- Example
- Sample Output
- When to Use
- Notes
- Related Commands

---

# Table of Contents

1. Daily Workflow
2. Terminal Basics
3. Navigation
4. File Management
5. Viewing Files
6. Searching
7. Permissions
8. System Information
9. Storage Management
10. Package Management
11. Conda
12. Python
13. Git
14. GitHub CLI
15. VS Code
16. Verilog Simulation
17. GTKWave
18. Keyboard Shortcuts
19. Troubleshooting
20. Best Practices
21. Appendix

---

# 1. Daily Workflow

A typical FPGA development session follows the same sequence every day.

```text
Open Ubuntu
      │
      ▼
Open Terminal
      │
      ▼
cd ~/FIR-Filter-FPGA
      │
      ▼
conda activate fir-fpga
      │
      ▼
code .
      │
      ▼
Write Verilog / Python
      │
      ▼
Compile
      │
      ▼
Simulate
      │
      ▼
View Waveforms
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
```

---

## Start Working

### Purpose

Prepare the development environment.

### Commands

```bash
cd ~/FIR-Filter-FPGA
conda activate fir-fpga
code .
```

### Expected Prompt

```text
(fir-fpga) abhi9@computer:~/FIR-Filter-FPGA$
```

### When to Use

At the beginning of every development session.

### Notes

Always activate the correct Conda environment before running Python scripts.

---

## End Working Session

### Commands

```bash
git status
git add .
git commit -m "Describe today's work"
git push
conda deactivate
```

### Purpose

Save changes, upload them to GitHub, and exit the Python environment.

---

# 2. Terminal Basics

The Linux terminal is a command-line interface that allows you to interact with the operating system efficiently.

---

# Print Working Directory (`pwd`)

## Purpose

Displays the absolute path of the current working directory.

## Syntax

```bash
pwd
```

## Example

```bash
pwd
```

## Sample Output

```text
/home/abhi9/FIR-Filter-FPGA/src
```

## When to Use

- Before compiling Verilog
- Before creating files
- When you are unsure where you are

## Notes

- `pwd` stands for **Print Working Directory**.
- This command does not modify any files.

## Related Commands

```bash
cd
ls
tree
```

---

# List Files (`ls`)

## Purpose

Displays files and folders inside the current directory.

## Syntax

```bash
ls
```

## Example

```bash
ls
```

## Sample Output

```text
README.md
src
testbench
python
results
paper
```

## Useful Options

Detailed list

```bash
ls -l
```

Show hidden files

```bash
ls -a
```

Detailed + hidden files

```bash
ls -la
```

Human-readable file sizes

```bash
ls -lh
```

## When to Use

- Check project contents
- Verify files exist
- Inspect directories

## Notes

Files beginning with a period (`.`) are hidden by default.

---

# Clear Screen (`clear`)

## Purpose

Clears the terminal window.

## Syntax

```bash
clear
```

Shortcut

```
Ctrl + L
```

## Notes

Does not delete command history.

---

# Command History (`history`)

## Purpose

Shows previously executed commands.

## Syntax

```bash
history
```

## Example Output

```text
101 cd ~/FIR-Filter-FPGA
102 git status
103 code .
104 conda activate fir-fpga
```

## Search History

Press

```
Ctrl + R
```

Type a keyword.

Example

```
git
```

The terminal searches previous Git commands.

---

# Stop a Running Program

Keyboard Shortcut

```
Ctrl + C
```

## Purpose

Terminates the currently running process.

Example

Stop a Python script.

Stop a simulation.

Stop an infinite loop.

---

# Exit Terminal

## Command

```bash
exit
```

or

```
Ctrl + D
```

## Purpose

Closes the current terminal session.

---

# Auto Completion

Press

```
Tab
```

Example

Instead of typing

```text
cd ~/FIR-Filter-FPGA
```

type

```text
cd ~/FI
```

then press

```
Tab
```

Linux completes the path automatically.

### Benefits

- Faster typing
- Fewer mistakes
- Discover available files and folders

---

# Command Line Editing

Move to beginning of line

```
Ctrl + A
```

Move to end of line

```
Ctrl + E
```

Delete previous word

```
Ctrl + W
```

Clear current line

```
Ctrl + U
```

These shortcuts significantly improve command-line productivity.

---

# Quick Reference

| Command | Purpose |
|----------|----------|
| pwd | Show current directory |
| ls | List files |
| ls -la | Detailed file list |
| clear | Clear terminal |
| history | View command history |
| exit | Close terminal |
| Ctrl+C | Stop running command |
| Ctrl+L | Clear screen |
| Ctrl+R | Search history |
| Tab | Auto-complete |
| Ctrl+A | Beginning of line |
| Ctrl+E | End of line |

---

# Chapter Summary

You learned how to:

- Check your current location
- List files
- Navigate command history
- Stop running commands
- Exit the terminal
- Use keyboard shortcuts to work more efficiently

These commands form the foundation of daily Linux usage.
---

# 3. Navigation

Navigation is the process of moving between directories (folders) in the Linux file system. Efficient navigation saves time and reduces mistakes.

---

# Change Directory (`cd`)

## Purpose

Changes the current working directory.

## Syntax

```bash
cd <directory>
```

## Examples

Go to your home directory:

```bash
cd ~
```

Go to the FPGA project:

```bash
cd ~/FIR-Filter-FPGA
```

Go to the source folder:

```bash
cd ~/FIR-Filter-FPGA/src
```

Go back one directory:

```bash
cd ..
```

Go to the previous directory:

```bash
cd -
```

Go to the root directory:

```bash
cd /
```

## When to Use

- Switching between project folders.
- Before compiling or editing files.
- Exploring the Linux filesystem.

## Notes

- `~` represents your home directory.
- `..` represents the parent directory.
- `/` represents the root directory.

---

# Absolute vs Relative Paths

## Absolute Path

Starts from the root (`/`).

Example:

```text
/home/abhi9/FIR-Filter-FPGA/src
```

Use absolute paths when you want to specify the exact location of a file.

---

## Relative Path

Starts from your current directory.

Example:

```bash
cd src
```

This only works if you are already inside the project directory.

---

# Display Directory Tree (`tree`)

## Purpose

Displays folders in a tree-like structure.

## Syntax

```bash
tree
```

Example

```text
FIR-Filter-FPGA
├── src
├── testbench
├── python
├── results
├── paper
└── README.md
```

## Install

```bash
sudo apt install tree
```

## When to Use

Understanding project structure.

---

# Hidden Files

Files beginning with a period (`.`) are hidden.

Show hidden files:

```bash
ls -a
```

Example

```text
.git
.gitignore
.vscode
```

These files usually contain configuration or project metadata.

---

# 4. File & Directory Management

Creating, copying, moving, renaming, and deleting files are essential Linux tasks.

---

# Create File (`touch`)

## Purpose

Creates an empty file or updates the timestamp of an existing file.

## Syntax

```bash
touch filename
```

## Example

Create a Verilog source file:

```bash
touch src/fir_filter.v
```

Create multiple files:

```bash
touch file1.txt file2.txt file3.txt
```

## When to Use

- Creating new source files.
- Creating documentation.
- Creating placeholder files.

---

# Create Directory (`mkdir`)

## Purpose

Creates a new directory.

## Syntax

```bash
mkdir directory_name
```

Example

```bash
mkdir documentation
```

Create nested directories:

```bash
mkdir -p project/src/testbench/results
```

## Notes

The `-p` option creates parent directories automatically.

---

# Copy Files (`cp`)

## Purpose

Copies files or directories.

## Syntax

```bash
cp source destination
```

Example

```bash
cp README.md backup_README.md
```

Copy a directory:

```bash
cp -r src backup_src
```

## Notes

- `-r` means recursive.
- Required when copying folders.

---

# Move or Rename (`mv`)

## Purpose

Moves or renames files.

## Syntax

```bash
mv source destination
```

Rename:

```bash
mv old.v fir_filter.v
```

Move file:

```bash
mv fir_filter.v src/
```

Move folder:

```bash
mv docs documentation
```

---

# Remove File (`rm`)

## Purpose

Deletes files permanently.

## Syntax

```bash
rm filename
```

Example

```bash
rm test.txt
```

Delete multiple files:

```bash
rm file1 file2 file3
```

## Warning

Linux does **not** move deleted files to a recycle bin. Deletion is permanent.

---

# Remove Directory (`rm -r`)

Delete folder and contents:

```bash
rm -r folder_name
```

Delete empty folder:

```bash
rmdir folder_name
```

### Dangerous Commands

Never run:

```bash
sudo rm -rf /
```

Never run:

```bash
sudo rm -rf ~
```

These commands can destroy your operating system or delete all files in your home directory.

---

# Wildcards

Linux supports wildcard characters.

## Asterisk (`*`)

Matches any number of characters.

Example

```bash
ls *.v
```

Shows all Verilog files.

Delete all text files:

```bash
rm *.txt
```

---

## Question Mark (`?`)

Matches one character.

Example

```bash
ls file?.txt
```

Matches:

```text
file1.txt
file2.txt
fileA.txt
```

---

# 5. Viewing Files

Linux provides several commands for reading file contents.

---

# Display Entire File (`cat`)

## Purpose

Displays the complete contents of a file.

## Syntax

```bash
cat filename
```

Example

```bash
cat README.md
```

## When to Use

- Reading small files.
- Checking configuration files.
- Viewing scripts.

---

# First Lines (`head`)

Displays the first lines of a file.

```bash
head filename
```

Display first 20 lines:

```bash
head -20 filename
```

Example

```bash
head README.md
```

---

# Last Lines (`tail`)

Displays the last lines of a file.

```bash
tail filename
```

Last 20 lines:

```bash
tail -20 filename
```

Monitor a growing log file:

```bash
tail -f simulation.log
```

Press **Ctrl+C** to stop monitoring.

---

# View Large Files (`less`)

Open a file:

```bash
less filename
```

Navigation:

- Arrow keys → Scroll
- Space → Next page
- b → Previous page
- / → Search
- q → Quit

Example

```bash
less README.md
```

---

# Count Lines, Words, and Characters (`wc`)

Display statistics:

```bash
wc filename
```

Example Output

```text
125 620 4890 README.md
```

Meaning:

- Lines
- Words
- Characters

Only line count:

```bash
wc -l README.md
```

---

# Number Lines (`nl`)

Display line numbers:

```bash
nl README.md
```

Useful when debugging code or referring to specific lines.

---

# Quick Reference

| Command | Purpose |
|----------|----------|
| cd | Change directory |
| cd .. | Parent directory |
| cd ~ | Home directory |
| cd - | Previous directory |
| tree | Show folder tree |
| touch | Create file |
| mkdir | Create folder |
| cp | Copy files |
| mv | Move or rename |
| rm | Delete file |
| rm -r | Delete folder |
| cat | Display file |
| head | First lines |
| tail | Last lines |
| less | View large file |
| wc | Count lines/words |
| nl | Number lines |

---

# Chapter Summary

In this section you learned how to:

- Navigate directories efficiently.
- Understand absolute and relative paths.
- Create, copy, move, rename, and delete files.
- Use wildcards for faster file operations.
- View small and large files.
- Count lines and inspect file contents.
- Avoid dangerous file deletion commands.

These commands are among the most frequently used during Linux development and FPGA projects.

---

# 6. Searching

Linux provides powerful commands for locating files and searching text inside files. These commands are especially useful when working with large FPGA projects.

---

# Find Files (`find`)

## Purpose

Searches for files and directories based on name, type, size, or other properties.

## Syntax

```bash
find <path> <options> <expression>
```

## Examples

Find all Verilog files:

```bash
find . -name "*.v"
```

Find all Python files:

```bash
find . -name "*.py"
```

Find Markdown files:

```bash
find . -name "*.md"
```

Find directories:

```bash
find . -type d
```

Find files only:

```bash
find . -type f
```

## Sample Output

```text
./src/fir_filter.v
./src/mac_unit.v
./testbench/tb_fir_filter.v
```

## When to Use

- Locate missing files.
- Search project folders.
- Verify generated files.

## Notes

- `.` means search from the current directory.
- Searches are case-sensitive.

---

# Search Text (`grep`)

## Purpose

Searches for text inside one or more files.

## Syntax

```bash
grep "text" filename
```

## Examples

Search for "module":

```bash
grep "module" src/fir_filter.v
```

Recursive search:

```bash
grep -rn "always" .
```

Ignore case:

```bash
grep -i "module" file.v
```

## Sample Output

```text
12:module fir_filter(
56:endmodule
```

## Useful Options

| Option | Description |
|---------|-------------|
| -r | Recursive search |
| -n | Show line numbers |
| -i | Ignore case |
| -v | Show lines that do not match |

## When to Use

- Find functions.
- Locate variables.
- Search Verilog modules.
- Search documentation.

---

# Locate Files (`locate`)

## Purpose

Finds files quickly using a database.

## Syntax

```bash
locate filename
```

Example

```bash
locate fir_filter.v
```

Update database:

```bash
sudo updatedb
```

## Notes

`locate` is faster than `find` but relies on an indexed database.

---

# Search Command History

Press

```
Ctrl + R
```

Type a keyword.

Example

```
iverilog
```

The terminal searches previously executed commands.

Press

```
Ctrl + R
```

again to continue searching.

---

# 7. File Permissions

Linux protects files using permissions.

Every file has:

- Owner
- Group
- Others

Each can have:

- Read (r)
- Write (w)
- Execute (x)

---

# View Permissions

```bash
ls -l
```

Example Output

```text
-rwxr-xr-- 1 abhi9 abhi9 1024 Jul 30 fir_filter.v
```

Meaning

```text
-rwxr-xr--
 │ │ │
 │ │ └── Others
 │ └──── Group
 └────── Owner
```

---

# Change Permissions (`chmod`)

## Purpose

Changes file permissions.

## Syntax

```bash
chmod permissions filename
```

Make executable:

```bash
chmod +x script.sh
```

Remove execute permission:

```bash
chmod -x script.sh
```

Numeric permission:

```bash
chmod 755 script.sh
```

## Common Values

| Value | Meaning |
|--------|----------|
| 777 | Full access |
| 755 | Owner full, others read/execute |
| 644 | Owner read/write, others read only |

---

# Change Ownership (`chown`)

## Purpose

Changes the owner of a file.

## Syntax

```bash
sudo chown user filename
```

Example

```bash
sudo chown abhi9 README.md
```

---

# Check Executable Files

```bash
ls -l *.sh
```

Executable files contain an `x`.

Example

```text
-rwxr-xr-x
```

---

# 8. System Information

Useful commands to inspect your Linux system.

---

# Ubuntu Version

```bash
lsb_release -a
```

Example Output

```text
Distributor ID: Ubuntu
Description: Ubuntu 24.04 LTS
```

---

# Kernel Version

```bash
uname -r
```

Example

```text
6.8.0-71-generic
```

---

# Machine Information

```bash
uname -a
```

Displays:

- Kernel
- Architecture
- Hostname
- Build information

---

# CPU Information

```bash
lscpu
```

Shows

- CPU model
- Number of cores
- Threads
- Cache
- Architecture

---

# Memory Usage

```bash
free -h
```

Example

```text
Mem: 15Gi 6.2Gi 7.8Gi
```

---

# Disk Usage

```bash
df -h
```

Shows

- Total disk
- Used
- Free space

Human-readable units:

- GB
- MB

---

# Current User

```bash
whoami
```

Example

```text
abhi9
```

---

# Hostname

```bash
hostname
```

Example

```text
ubuntu
```

---

# Current Date and Time

```bash
date
```

Example

```text
Thu Jul 31 11:30:42 IST 2026
```

---

# 9. Disk & Storage Management

Monitor storage usage to avoid running out of space.

---

# Disk Usage

```bash
df -h
```

Shows mounted drives and available storage.

---

# Directory Size

```bash
du -sh .
```

Current directory size.

Project size:

```bash
du -sh ~/FIR-Filter-FPGA
```

---

# Largest Files

```bash
du -sh * | sort -hr
```

Displays directories sorted from largest to smallest.

---

# List Storage Devices

```bash
lsblk
```

Example

```text
NAME
sda
├── sda1
├── sda2
└── sda3
```

Useful for checking disks and USB drives.

---

# Mounted Filesystems

```bash
mount
```

Displays all mounted devices.

---

# Available Space in Home

```bash
df -h ~
```

Shows remaining space for your project files.

---

# Quick Reference

| Command | Purpose |
|----------|----------|
| find | Search files |
| grep | Search text |
| locate | Fast file search |
| ls -l | View permissions |
| chmod | Change permissions |
| chown | Change ownership |
| uname | Kernel information |
| lscpu | CPU information |
| free -h | Memory usage |
| df -h | Disk usage |
| du -sh | Folder size |
| lsblk | Storage devices |
| hostname | Computer name |
| whoami | Current user |
| date | Current date and time |

---

# Chapter Summary

In this section you learned how to:

- Search for files using `find`.
- Search text using `grep`.
- Use `locate` for fast file searches.
- Understand Linux file permissions.
- Make scripts executable.
- View CPU, memory, and kernel information.
- Monitor disk usage and available storage.

These commands are essential for managing Linux systems and maintaining FPGA development projects.

---

# 10. Package Management (APT)

APT (Advanced Package Tool) is Ubuntu's package management system. It is used to install, update, upgrade, and remove software packages.

---

# Update Package List (`apt update`)

## Purpose

Downloads the latest package information from Ubuntu repositories.

## Syntax

```bash
sudo apt update
```

## Example

```bash
sudo apt update
```

## Sample Output

```text
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Reading package lists... Done
```

## When to Use

- Before installing new software.
- Before upgrading packages.
- At least once every few weeks.

## Notes

- Does **not** install updates.
- Only refreshes the package database.

---

# Upgrade Installed Packages (`apt upgrade`)

## Purpose

Upgrades installed software to the latest available versions.

## Syntax

```bash
sudo apt upgrade
```

## Example

```bash
sudo apt upgrade
```

## When to Use

- After running `sudo apt update`.
- To keep Ubuntu secure and up to date.

---

# Install a Package (`apt install`)

## Purpose

Installs new software.

## Syntax

```bash
sudo apt install package-name
```

## Examples

Install Git

```bash
sudo apt install git
```

Install Tree

```bash
sudo apt install tree
```

Install Java

```bash
sudo apt install openjdk-17-jdk
```

Install Python Pip

```bash
sudo apt install python3-pip
```

---

# Remove Package (`apt remove`)

## Purpose

Removes installed software while keeping configuration files.

## Syntax

```bash
sudo apt remove package-name
```

Example

```bash
sudo apt remove tree
```

---

# Completely Remove Package (`apt purge`)

## Purpose

Removes software and its configuration files.

## Syntax

```bash
sudo apt purge package-name
```

Example

```bash
sudo apt purge tree
```

---

# Remove Unused Packages

```bash
sudo apt autoremove
```

Purpose

Deletes packages no longer required.

---

# Clean Download Cache

```bash
sudo apt clean
```

Purpose

Deletes downloaded installation files to free disk space.

---

# Search for Packages

```bash
apt search package-name
```

Example

```bash
apt search verilog
```

---

# Installed Package Information

```bash
apt show package-name
```

Example

```bash
apt show git
```

---

# 11. Conda Environment

Conda manages isolated Python environments. Your FPGA project uses the **fir-fpga** environment.

---

# Check Conda Version

```bash
conda --version
```

Example Output

```text
conda 25.x.x
```

---

# List Environments

```bash
conda env list
```

Example

```text
base
fir-fpga
```

Current environment has an asterisk (`*`).

---

# Activate Environment

## Purpose

Switch to the FPGA Python environment.

```bash
conda activate fir-fpga
```

Expected Prompt

```text
(fir-fpga) abhi9@computer:~/FIR-Filter-FPGA$
```

---

# Deactivate Environment

```bash
conda deactivate
```

Returns to

```text
(base)
```

or no active environment.

---

# Create Environment

```bash
conda create -n fir-fpga python=3.12
```

Purpose

Creates a new isolated Python environment.

---

# Remove Environment

```bash
conda env remove -n environment-name
```

Example

```bash
conda env remove -n test-env
```

---

# Install Package

```bash
conda install numpy
```

Install Multiple Packages

```bash
conda install numpy scipy matplotlib pandas
```

---

# Update Package

```bash
conda update numpy
```

---

# Update Conda

```bash
conda update conda
```

---

# List Installed Packages

```bash
conda list
```

Useful for checking installed libraries.

---

# Export Environment

```bash
conda env export > environment.yml
```

Purpose

Creates a backup of the environment.

---

# Recreate Environment

```bash
conda env create -f environment.yml
```

Useful when moving the project to another computer.

---

# 12. Python Commands

Python is used to design FIR filters, generate coefficients, analyze signals, and verify Verilog simulations.

---

# Check Python Version

```bash
python --version
```

Example

```text
Python 3.12.11
```

---

# Run Python Script

```bash
python script.py
```

Example

```bash
python python/generate_coefficients.py
```

---

# Interactive Python

```bash
python
```

Example

```python
>>> print("Hello FPGA")
Hello FPGA
```

Exit

```python
exit()
```

or

```
Ctrl+D
```

---

# Run Python Module

```bash
python -m module_name
```

Example

```bash
python -m pip --version
```

---

# Install Packages Using Pip

Although Conda is recommended, pip can also be used.

```bash
pip install package-name
```

Example

```bash
pip install scipy
```

---

# List Installed Pip Packages

```bash
pip list
```

---

# Freeze Installed Packages

```bash
pip freeze
```

Save to file

```bash
pip freeze > requirements.txt
```

---

# Install from Requirements File

```bash
pip install -r requirements.txt
```

---

# Test Installed Libraries

```bash
python -c "import numpy, scipy, matplotlib, pandas"
```

If nothing is printed, all libraries loaded successfully.

---

# Start Jupyter Notebook

```bash
jupyter notebook
```

Starts a local notebook server in your web browser.

---

# Start JupyterLab

```bash
jupyter lab
```

Modern interface for notebooks and file management.

---

# Useful Python Libraries

| Library | Purpose |
|----------|----------|
| NumPy | Numerical computing |
| SciPy | Signal processing |
| Matplotlib | Plotting graphs |
| Pandas | Data analysis |
| Jupyter | Interactive notebooks |

---

# Quick Reference

| Command | Purpose |
|----------|----------|
| sudo apt update | Refresh package list |
| sudo apt upgrade | Upgrade packages |
| sudo apt install | Install software |
| sudo apt remove | Remove software |
| sudo apt autoremove | Remove unused packages |
| sudo apt clean | Clear package cache |
| conda activate | Activate environment |
| conda deactivate | Exit environment |
| conda list | Installed packages |
| conda env list | List environments |
| python --version | Python version |
| python script.py | Run script |
| python | Interactive Python |
| pip list | Installed pip packages |
| jupyter notebook | Start Jupyter |

---

# Chapter Summary

In this section you learned how to:

- Update and install Ubuntu software using APT.
- Manage Conda environments.
- Install and update Python packages.
- Run Python scripts.
- Launch Jupyter Notebook and JupyterLab.
- Export and recreate Conda environments.
- Verify installed Python libraries.

These commands are essential for maintaining your Python environment and supporting the FPGA FIR filter development workflow.

---

# 13. Git & GitHub

Git is a distributed version control system used to track changes in files, collaborate with others, and maintain a history of your project.

GitHub is an online platform used to host Git repositories.

---

# What is Version Control?

Version control allows you to:

- Track changes made to files.
- Restore previous versions.
- Work safely without losing code.
- Collaborate with others.
- Maintain a complete project history.

Example:

```text
Version 1.0
      │
      ▼
Added FIR Filter
      │
      ▼
Added Testbench
      │
      ▼
Optimized Architecture
      │
      ▼
Fixed Timing Issue
```

---

# Initialize Repository (`git init`)

## Purpose

Creates a new Git repository.

## Syntax

```bash
git init
```

## Example

```bash
cd FIR-Filter-FPGA
git init
```

## Sample Output

```text
Initialized empty Git repository
```

## When to Use

Only once when starting a new project.

---

# Clone Repository (`git clone`)

## Purpose

Downloads an existing GitHub repository.

## Syntax

```bash
git clone repository-url
```

## Example

```bash
git clone https://github.com/username/FIR-Filter-FPGA.git
```

---

# Repository Status (`git status`)

## Purpose

Displays the current state of the repository.

## Syntax

```bash
git status
```

## Example

```bash
git status
```

## Sample Output

```text
On branch main

Changes not staged for commit:

modified: src/fir_filter.v
```

## When to Use

- Before committing
- Before pushing
- Before pulling

---

# Add Files (`git add`)

## Purpose

Stages files for the next commit.

## Syntax

```bash
git add filename
```

Stage one file

```bash
git add README.md
```

Stage all files

```bash
git add .
```

## Notes

Only staged files become part of the next commit.

---

# Commit Changes (`git commit`)

## Purpose

Saves staged changes into the Git history.

## Syntax

```bash
git commit -m "Commit message"
```

## Example

```bash
git commit -m "Implemented direct-form FIR filter"
```

## Good Commit Messages

```text
Added FIR coefficient generator

Fixed overflow bug

Created testbench

Updated documentation
```

## Poor Commit Messages

```text
Update

Test

abc

Changes
```

Always write meaningful commit messages.

---

# View Commit History (`git log`)

Show complete history

```bash
git log
```

Compact history

```bash
git log --oneline
```

Example

```text
a42c381 Added FIR coefficients
98bc421 Created testbench
```

---

# Undo Last Commit (Keep Changes)

```bash
git reset --soft HEAD~1
```

Useful if you committed too early.

---

# Restore File

Discard local modifications.

```bash
git restore filename
```

Example

```bash
git restore README.md
```

---

# Branches

Show branches

```bash
git branch
```

Create branch

```bash
git branch feature-filter
```

Switch branch

```bash
git switch feature-filter
```

Create and switch

```bash
git switch -c feature-filter
```

Delete branch

```bash
git branch -d feature-filter
```

---

# Merge Branch

Merge another branch into the current branch.

```bash
git merge feature-filter
```

---

# Remote Repository

View remotes

```bash
git remote -v
```

Example

```text
origin
https://github.com/username/FIR-Filter-FPGA.git
```

---

# Push Changes

Upload commits to GitHub.

```bash
git push
```

First push

```bash
git push -u origin main
```

---

# Pull Changes

Download latest changes.

```bash
git pull
```

Always pull before starting work if using multiple computers.

---

# Fetch Changes

Download updates without merging.

```bash
git fetch
```

Useful when you want to inspect changes first.

---

# Clone vs Pull

| Command | Purpose |
|----------|----------|
| git clone | Download repository for the first time |
| git pull | Update existing repository |

---

# Git Ignore

Git ignores files listed in `.gitignore`.

Example

```text
__pycache__/
*.pyc
*.vcd
*.log
*.tmp
```

Useful for excluding generated files.

---

# Useful Git Workflow

```text
Edit Files
     │
     ▼
git status
     │
     ▼
git add .
     │
     ▼
git commit -m "Meaningful message"
     │
     ▼
git push
```

---

# GitHub CLI (gh)

GitHub CLI lets you work with GitHub directly from the terminal.

Check version

```bash
gh --version
```

Login

```bash
gh auth login
```

Authentication status

```bash
gh auth status
```

Logout

```bash
gh auth logout
```

Clone repository

```bash
gh repo clone username/FIR-Filter-FPGA
```

Open repository in browser

```bash
gh repo view --web
```

---

# Best Practices

✅ Commit frequently.

✅ Write meaningful commit messages.

✅ Push after completing a logical feature.

✅ Pull before starting work on another computer.

✅ Keep documentation updated.

✅ Never commit passwords or API keys.

✅ Use `.gitignore` for generated files.

---

# Common Mistakes

❌ Forgetting to commit changes.

❌ Using meaningless commit messages.

❌ Editing directly on GitHub without pulling.

❌ Deleting `.git` accidentally.

❌ Committing generated simulation files.

---

# Quick Reference

| Command | Purpose |
|----------|----------|
| git init | Create repository |
| git clone | Download repository |
| git status | Check repository status |
| git add | Stage files |
| git commit | Save changes |
| git log | View history |
| git restore | Restore file |
| git branch | List branches |
| git switch | Switch branch |
| git merge | Merge branches |
| git remote -v | View remote |
| git fetch | Download changes |
| git pull | Download and merge |
| git push | Upload changes |
| gh auth login | Login to GitHub |
| gh repo clone | Clone using GitHub CLI |

---

# Chapter Summary

You learned how to:

- Create and clone Git repositories.
- Track project changes.
- Stage and commit files.
- View commit history.
- Work with branches.
- Synchronize with GitHub.
- Use GitHub CLI.
- Follow professional Git workflows for FPGA development.

---

# 14. Visual Studio Code (VS Code)

Visual Studio Code is the primary editor used for this FPGA project. It supports Verilog, Python, Git, Markdown, and many useful extensions.

---

# Open VS Code

## Purpose

Launch VS Code from the terminal.

## Syntax

```bash
code .
```

## Example

```bash
cd ~/FIR-Filter-FPGA
code .
```

Opens the current project folder.

---

# Open a Specific File

```bash
code README.md
```

Open multiple files

```bash
code README.md src/fir_filter.v
```

---

# Check Version

```bash
code --version
```

---

# List Installed Extensions

```bash
code --list-extensions
```

---

# Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| Python | Python support |
| Pylance | IntelliSense |
| Verilog HDL/SystemVerilog | Verilog syntax highlighting |
| GitLens | Enhanced Git integration |
| Markdown All in One | Markdown editing |

---

# Useful Keyboard Shortcuts

| Shortcut | Purpose |
|-----------|---------|
| Ctrl+P | Open file |
| Ctrl+Shift+P | Command Palette |
| Ctrl+Shift+V | Markdown Preview |
| Ctrl+` | Toggle Terminal |
| Ctrl+/ | Comment line |
| Ctrl+S | Save |
| Ctrl+F | Find |
| Ctrl+H | Replace |

---

# 15. Verilog Simulation (Icarus Verilog)

Icarus Verilog is an open-source Verilog compiler and simulator.

---

# Check Version

```bash
iverilog -V
```

---

# Compile Verilog

## Syntax

```bash
iverilog -o output source_files
```

## Example

```bash
iverilog -o sim.out src/*.v testbench/*.v
```

Creates an executable simulation file named `sim.out`.

---

# Run Simulation

```bash
vvp sim.out
```

---

# Redirect Output to a Log

```bash
vvp sim.out > simulation.log
```

View the log

```bash
cat simulation.log
```

---

# Common Simulation Workflow

```text
Write Verilog
      │
      ▼
Compile (iverilog)
      │
      ▼
Run (vvp)
      │
      ▼
Generate waveform.vcd
      │
      ▼
Open GTKWave
```

---

# 16. GTKWave

GTKWave is used to inspect simulation waveforms.

---

# Open Waveform

```bash
gtkwave waveform.vcd
```

---

# Check Version

```bash
gtkwave --version
```

---

# Useful Tips

- Zoom in/out using the mouse wheel.
- Drag signals into the waveform window.
- Save waveform layouts for reuse.

---

# 17. Useful Aliases

Aliases create shortcuts for long commands.

Open your shell configuration:

```bash
nano ~/.bashrc
```

Add the following:

```bash
alias fpga='cd ~/FIR-Filter-FPGA'
alias codefpga='cd ~/FIR-Filter-FPGA && conda activate fir-fpga && code .'
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline'
alias ll='ls -lah'
```

Reload the shell:

```bash
source ~/.bashrc
```

Examples

```bash
fpga
codefpga
gs
gp
```

---

# 18. Troubleshooting

## `conda: command not found`

Reload your shell:

```bash
source ~/.bashrc
```

If necessary, restart the terminal.

---

## Environment Not Found

List environments:

```bash
conda env list
```

Activate the correct one:

```bash
conda activate fir-fpga
```

---

## Git Push Rejected

Pull the latest changes first:

```bash
git pull
```

Resolve any merge conflicts, then push again.

---

## `code: command not found`

Open VS Code and install the `code` command from the Command Palette:

```
Shell Command: Install 'code' command in PATH
```

Restart the terminal.

---

## `iverilog: command not found`

Install Icarus Verilog:

```bash
sudo apt install iverilog
```

Verify installation:

```bash
iverilog -V
```

---

## `gtkwave: command not found`

Install GTKWave:

```bash
sudo apt install gtkwave
```

Verify installation:

```bash
gtkwave --version
```

---

# 19. Best Practices

## Linux

- Keep your system updated.
- Organize project files into folders.
- Avoid running commands with `sudo` unless necessary.

## Git

- Commit small, meaningful changes.
- Write descriptive commit messages.
- Push your work regularly.

## Python

- Always activate the `fir-fpga` environment before running scripts.
- Keep required packages documented.

## FPGA Development

- Separate source files and testbenches.
- Store simulation outputs in the `results/` directory.
- Verify simulation before synthesis.
- Document design decisions and test results.

---

# 20. Daily FPGA Workflow

```text
Start Ubuntu
      │
      ▼
Open Terminal
      │
      ▼
cd ~/FIR-Filter-FPGA
      │
      ▼
conda activate fir-fpga
      │
      ▼
code .
      │
      ▼
Edit Verilog / Python
      │
      ▼
iverilog -o sim.out src/*.v testbench/*.v
      │
      ▼
vvp sim.out
      │
      ▼
gtkwave waveform.vcd
      │
      ▼
Verify Results
      │
      ▼
git status
      │
      ▼
git add .
      │
      ▼
git commit -m "Meaningful message"
      │
      ▼
git push
      │
      ▼
conda deactivate
```

---

# Final Notes

This handbook is intended to be a living document.

As you learn new Linux commands, Git workflows, Python techniques, or FPGA tools, add them here with:

- Purpose
- Syntax
- Example
- Notes
- Related Commands

Over time, this will become your own personalized Linux and FPGA reference guide.

---

**Document Version:** 1.0  
**Last Updated:** July 2026

---

21. Appendix

The appendix contains additional reference material that supports the main handbook.

---

# Appendix A – Linux File System

## Common Directories

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
│   └── abhi9
│       └── FIR-Filter-FPGA
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── srv
├── sys
├── tmp
├── usr
└── var
```

| Directory | Purpose |
|-----------|---------|
| `/home` | User files |
| `/etc` | System configuration |
| `/usr` | Installed applications |
| `/bin` | Essential commands |
| `/tmp` | Temporary files |
| `/var` | Logs and variable data |

---

# Appendix B – Useful File Extensions

| Extension | Description |
|-----------|-------------|
| `.v` | Verilog source file |
| `.sv` | SystemVerilog file |
| `.vcd` | Waveform output |
| `.py` | Python script |
| `.md` | Markdown document |
| `.txt` | Plain text |
| `.pdf` | PDF document |
| `.gitignore` | Git ignore rules |
| `.yml` | Conda/GitHub configuration |

---

# Appendix C – Common Linux Errors

## Permission Denied

**Cause**

File is not executable.

**Solution**

```bash
chmod +x filename
```

---

## Command Not Found

**Cause**

The program is not installed or not in your PATH.

**Solution**

```bash
which command_name
```

or

```bash
sudo apt install package-name
```

---

# Appendix D – FPGA Project Folder Structure

```text
FIR-Filter-FPGA/
│
├── src/
├── testbench/
├── python/
├── constraints/
├── results/
├── paper/
│
├── README.md
├── Linux_Command_CheatSheet.md
├── Git_CheatSheet.md
├── Verilog_CheatSheet.md
├── Python_FIR_Notes.md
├── Vivado_Workflow.md
├── ISE_Workflow.md
├── FPGA_Project_Log.md
└── Project_Roadmap.md
```

---

# Appendix E – Useful Terminal Tips

- Press **Tab** to auto-complete commands and filenames.
- Press **Ctrl + R** to search command history.
- Press **Ctrl + C** to stop a running process.
- Press **Ctrl + L** to clear the terminal.
- Use `history` to view previously executed commands.

---

# Document Information

**Document:** Linux_Command_CheatSheet.md

**Version:** 1.0

**Maintained By:** Abhinav

**Project:** FPGA Implementation of Optimized FIR Filter for Signal Processing

**Last Updated:** July 2026