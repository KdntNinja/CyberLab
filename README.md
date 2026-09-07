# Cyberlab

Cyberlab is my A-Level Computer Science project.

The idea is to make a smaller self-hosted cybersecurity training platform inspired by TryHackMe, where users can
complete rooms, answer questions, launch isolated lab environments, track progress, and earn points.

I want the main focus to be on the actual platform and backend systems rather than making loads of challenge content.

---

## What I want it to do

* [ ] User accounts
* [ ] Login/logout
* [ ] Cybersecurity rooms
* [ ] Tasks/questions inside rooms
* [ ] Flag/answer checking
* [ ] Progress tracking
* [ ] Points
* [ ] Leaderboard
* [ ] Room prerequisites
* [ ] Docker-based challenge environments
* [ ] Challenge start/stop system
* [ ] Basic recommendations for what room to do next

---

# Development Rules

Before I commit anything:

* [ ] Ruff passes
* [ ] Ruff formatting passes
* [ ] Pyright strict passes
* [ ] Pytest passes
* [ ] New features have tests where needed
* [ ] No random `Any` types unless genuinely unavoidable
* [ ] No secrets committed
* [ ] Docker logic stays out of Django views
* [ ] Users cannot launch arbitrary Docker images
* [ ] Changes are small enough that I can explain them in my NEA write-up

Current checks:

```bash id="lxu1de"
./.venv/bin/ruff check . &&
./.venv/bin/ruff format --check . &&
./.venv/bin/pyright &&
./.venv/bin/pytest --suppress-no-test-exit-code
```

---

# Roadmap

## 0. Initial Setup

* [x] Create project
* [x] Initialise Git
* [x] Initialise uv
* [x] Create `.venv`
* [x] Add Ruff
* [x] Add Ruff formatting
* [x] Add Pyright strict
* [x] Add pytest
* [x] Add pre-commit
* [x] Remove default PyCharm `main.py`
* [x] Install Django
* [x] Create Django project
* [x] Make sure Django runs
* [x] Add first actual test
* [x] Remove temporary "allow zero tests" setting

Done when:

> Django runs and all project checks pass.

---

## 1. Basic Project Structure

Create the main Django apps.

* [ ] `accounts`
* [ ] `rooms`
* [ ] `progress`
* [ ] `challenges`
* [ ] `leaderboard`

Basic structure I want:

```text id="p9a3gq"
cyberlab/
├── config/
├── accounts/
├── rooms/
├── progress/
├── challenges/
├── leaderboard/
├── templates/
├── static/
└── tests/
```

Then:

* [ ] Set up URLs
* [ ] Set up templates
* [ ] Set up static files
* [ ] Add Bootstrap
* [ ] Make a basic base template
* [ ] Add navigation

Done when:

> I have an empty but properly structured website with working navigation.

---

## 2. Accounts

* [ ] Registration
* [ ] Login
* [ ] Logout
* [ ] Profile page
* [ ] Protect pages that need login
* [ ] Test registration
* [ ] Test duplicate usernames
* [ ] Test login/logout
* [ ] Test protected pages

Done when:

> I can create an account, log in, log out, and view my profile.

---

## 3. Rooms

Start making the main room system.

Each room should have:

* [ ] Title
* [ ] Slug
* [ ] Description
* [ ] Difficulty
* [ ] Category
* [ ] Points
* [ ] Enabled/disabled state

Then:

* [ ] Create room model
* [ ] Add rooms to Django Admin
* [ ] Make room list page
* [ ] Make room detail page
* [ ] Show difficulty
* [ ] Show category
* [ ] Add basic filtering
* [ ] Add tests

Done when:

> I can create rooms in the admin panel and browse them normally.

---

## 4. Tasks

Rooms need tasks/questions.

Each task should have:

* [ ] Room
* [ ] Order/number
* [ ] Title
* [ ] Instructions
* [ ] Correct answer
* [ ] Points
* [ ] Optional hint

Then:

* [ ] Task model
* [ ] Show tasks inside rooms
* [ ] Answer submission
* [ ] Correct answer handling
* [ ] Incorrect answer handling
* [ ] Prevent duplicate completion
* [ ] Tests

Done when:

> I can complete tasks inside a room.

---

## 5. Progress Tracking

* [ ] Track completed tasks
* [ ] Store completion time
* [ ] Count attempts
* [ ] Calculate room percentage
* [ ] Mark rooms as completed
* [ ] Show progress on room page
* [ ] Show progress on profile
* [ ] Tests

Done when:

> My progress stays saved when I leave and come back.

---

## 6. Scoring

Keep this simple at first.

* [ ] Award points for first completion
* [ ] Prevent duplicate points
* [ ] Calculate total score
* [ ] Show score on profile
* [ ] Tests

Done when:

> Completing tasks correctly updates my score.

---

## 7. Room Prerequisites

I want rooms to unlock in a proper learning path.

Example:

```text id="8c9s2e"
Linux Basics
    ↓
Networking
    ↓
Enumeration
```

Need to add:

* [ ] Prerequisite model
* [ ] Show locked rooms
* [ ] Check prerequisites
* [ ] Stop users opening locked rooms
* [ ] Prevent circular dependencies
* [ ] Store room relationships as a graph
* [ ] Use graph traversal
* [ ] Tests

Potential algorithms:

* [ ] BFS
* [ ] DFS
* [ ] Cycle detection

Done when:

> Rooms can depend on other rooms without breaking the learning path.

---

## 8. Leaderboard

* [ ] Global leaderboard
* [ ] Sort by score
* [ ] Handle ties
* [ ] Show rank
* [ ] Tests

Done when:

> Users can compare scores properly.

---

## 9. Challenge System

Before touching Docker properly, make the challenge logic clean first.

I want a `ChallengeManager` responsible for:

* [ ] Starting challenges
* [ ] Stopping challenges
* [ ] Checking challenge status
* [ ] Expiring challenges
* [ ] Linking challenge to user
* [ ] Linking challenge to room

Possible states:

```text id="cr9gdv"
STOPPED
STARTING
RUNNING
STOPPING
FAILED
```

* [ ] Use Enum for states
* [ ] Test state changes
* [ ] Keep Docker-specific code separate

Done when:

> Challenge lifecycle logic works even without real Docker containers.

---

## 10. Docker Integration

Only start this once the normal platform works.

* [ ] Add Docker SDK
* [ ] Connect to Docker
* [ ] Start approved container
* [ ] Stop container
* [ ] Detect status
* [ ] Assign temporary port
* [ ] Save container ID
* [ ] Link container to user
* [ ] Prevent duplicate instances
* [ ] Handle failed starts
* [ ] Handle unexpected shutdown
* [ ] Add resource limits
* [ ] Add timeout
* [ ] Clean up expired containers
* [ ] Tests/mocks

Security rules:

* [ ] No arbitrary Docker image input
* [ ] No privileged challenge containers
* [ ] No unnecessary host mounts
* [ ] No Docker socket inside challenge containers
* [ ] Restrict networking where sensible

Done when:

> A user can start and stop an isolated challenge environment safely.

---

## 11. First Proper Challenge

Do one full room before making loads of content.

Probably:

```text id="9xy6of"
Linux Fundamentals
```

Need to:

* [ ] Create Docker image
* [ ] Create room
* [ ] Create tasks
* [ ] Start environment
* [ ] Complete it manually
* [ ] Submit answers
* [ ] Track progress
* [ ] Stop environment
* [ ] Test entire flow

Done when:

> One complete room works from start to finish.

---

## 12. More Rooms

Only add more once the first room is solid.

Ideas:

* [ ] Linux Fundamentals
* [ ] Networking Fundamentals
* [ ] HTTP Fundamentals
* [ ] Web Enumeration
* [ ] File Permissions
* [ ] Weak Authentication
* [ ] Log Analysis
* [ ] Basic Cryptography

Important:

> Do not waste loads of NEA time making challenge content. The platform is the actual project.

---

## 13. Search and Filtering

* [ ] Search room titles
* [ ] Filter by category
* [ ] Filter by difficulty
* [ ] Filter completed/incomplete
* [ ] Filter locked/unlocked
* [ ] Sort rooms
* [ ] Tests

Could potentially compare different search/sort approaches for the write-up.

---

## 14. Recommendations

Only if the core project is finished.

Possible inputs:

* [ ] Difficulty
* [ ] Completed rooms
* [ ] Failed attempts
* [ ] Weak categories
* [ ] Prerequisites
* [ ] Previous activity

Need to:

* [ ] Design recommendation algorithm
* [ ] Rank rooms
* [ ] Never recommend locked rooms
* [ ] Explain why a room was recommended
* [ ] Tests

Done when:

> The dashboard can suggest a sensible next room.

---

## 15. UI

Leave most visual polish until later.

* [ ] Responsive navigation
* [ ] Dashboard
* [ ] Room cards
* [ ] Difficulty badges
* [ ] Progress bars
* [ ] Challenge status
* [ ] Error pages
* [ ] Better validation messages
* [ ] Minimal custom CSS

Try to use Bootstrap instead of spending ages on frontend work.

---

## 16. Testing Pass

Before calling the project finished:

* [ ] Model tests
* [ ] Authentication tests
* [ ] Task validation tests
* [ ] Progress tests
* [ ] Score tests
* [ ] Prerequisite tests
* [ ] Graph/cycle tests
* [ ] Challenge lifecycle tests
* [ ] Docker failure tests
* [ ] Permission tests
* [ ] Invalid input tests
* [ ] End-to-end tests

Run:

```bash id="yfr2an"
pytest
```

and:

```bash id="b28h8e"
pytest --cov
```

---

## 17. Final Security Check

* [ ] No passwords in code
* [ ] No secret keys in code
* [ ] `.env` ignored
* [ ] Debug disabled outside development
* [ ] CSRF enabled
* [ ] Authentication required where needed
* [ ] Users cannot modify other users' progress
* [ ] Users cannot award themselves points
* [ ] Answers/flags are not leaked into HTML
* [ ] Docker images are server controlled
* [ ] Containers have limits
* [ ] Containers expire
* [ ] User input is validated
* [ ] Errors do not leak sensitive information

---

# How I want to work on features

For each feature:

```text id="iopfl6"
Pick one small feature
        ↓
Work out what it needs to do
        ↓
Design it
        ↓
Write tests where useful
        ↓
Implement it
        ↓
Run all checks
        ↓
Test it manually
        ↓
Update NEA notes
        ↓
Commit
```

Try not to make massive commits.

Good:

```text id="xvfqhu"
Add room model

Add task validation

Add progress tracking

Add prerequisite cycle detection
```

Bad:

```text id="06fuf5"
stuff

changes

big update

fixed things
```

---

# Before Every Commit

```bash id="3b7yz8"
./.venv/bin/ruff check .
./.venv/bin/ruff format --check .
./.venv/bin/pyright
./.venv/bin/pytest
```

Then:

```bash id="1gwwip"
git status
git add .
git commit
```

---

# Current Focus

## Working On

* [ ] Set up Django

## Next

* [ ] Create project structure
* [ ] Add first test
* [ ] Set up accounts
* [ ] Start room system

## Blocked

Nothing currently.

---

# MVP

I will consider the core project finished when:

* [ ] Users can register/login
* [ ] Rooms work
* [ ] Rooms contain tasks
* [ ] Answers can be submitted
* [ ] Progress saves
* [ ] Scores work
* [ ] Prerequisites work
* [ ] One Docker challenge launches
* [ ] One full room works end-to-end
* [ ] Tests cover the core system
* [ ] All checks pass

Anything after that is extra.
