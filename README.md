# Cyberlab

Cyberlab is my A-Level Computer Science project.

The aim is to build a small self-hosted cybersecurity training platform inspired by TryHackMe, with rooms, tasks,
progress tracking, scoring, and isolated Docker challenge environments.

The main focus is the platform and backend systems rather than creating lots of challenge content.

---

## Main Features

* [ ] User accounts
* [ ] Login/logout
* [ ] Cybersecurity rooms
* [ ] Tasks and flag checking
* [ ] Progress tracking
* [ ] Points and leaderboard
* [ ] Room prerequisites
* [ ] Docker challenge environments
* [ ] Challenge start/stop system
* [ ] Basic room recommendations

---

## Development Rules

Before committing:

* [ ] Ruff passes
* [ ] Ruff formatting passes
* [ ] Pyright strict passes
* [ ] Pytest passes
* [ ] New features have tests where useful
* [ ] No secrets committed
* [ ] Avoid unnecessary `Any`
* [ ] Keep Docker logic separate from Django views
* [ ] Do not allow arbitrary Docker images

Run:

```bash
./.venv/bin/ruff check . &&
./.venv/bin/ruff format --check . &&
./.venv/bin/pyright &&
./.venv/bin/pytest
```

---

## Roadmap

## 0. Setup

* [x] Git + uv project
* [x] `.venv`
* [x] Ruff
* [x] Pyright strict
* [x] pytest
* [x] pre-commit
* [x] Django project
* [x] Development/production settings
* [x] Environment-based secrets
* [x] Production static-file setup
* [x] First tests

---

## 1. Project Structure

* [x] `accounts`
* [x] `rooms`
* [x] `progress`
* [x] `challenges`
* [x] `leaderboard`
* [x] Shared templates
* [x] Static files
* [x] Bootstrap
* [x] Base template
* [x] Homepage
* [x] Basic navigation
* [x] Homepage tests

---

## 2. Accounts

* [x] Registration
* [x] Login
* [x] Logout
* [x] Profile page
* [x] Protected pages
* [x] Account tests

Done when:

> Users can create an account, log in, and view their profile.

---

## 3. Rooms and Tasks

* [x] Room model
* [x] Categories and difficulty
* [x] Room list
* [x] Room detail page
* [x] Task model
* [ ] Answer submission
* [ ] Flag checking
* [ ] Hints
* [ ] Tests

Done when:

> Rooms can be created and users can complete tasks inside them.

---

## 4. Progress and Scoring

* [ ] Track completed tasks
* [ ] Track attempts
* [ ] Room completion percentage
* [ ] Completed rooms
* [ ] Award points
* [ ] Prevent duplicate points
* [ ] User score
* [ ] Tests

Done when:

> Progress and scores persist between sessions.

---

## 5. Prerequisites and Leaderboard

* [ ] Room prerequisites
* [ ] Locked/unlocked rooms
* [ ] Prevent circular dependencies
* [ ] Graph traversal
* [ ] Leaderboard
* [ ] Ranking and ties
* [ ] Tests

Algorithms to consider:

* BFS
* DFS
* Cycle detection

---

## 6. Challenge System

Build the challenge lifecycle before Docker integration.

* [ ] `ChallengeManager`
* [ ] Start challenge
* [ ] Stop challenge
* [ ] Challenge status
* [ ] Expiry
* [ ] Link challenge to user
* [ ] Link challenge to room
* [ ] State enum
* [ ] Tests

Possible states:

```text
STOPPED
STARTING
RUNNING
STOPPING
FAILED
```

---

## 7. Docker Integration

* [ ] Connect to Docker
* [ ] Start approved container
* [ ] Stop container
* [ ] Assign temporary port
* [ ] Store container ID
* [ ] Prevent duplicate instances
* [ ] Handle failures
* [ ] Add resource limits
* [ ] Add timeouts
* [ ] Clean expired containers
* [ ] Tests/mocks

Security:

* [ ] No arbitrary Docker images
* [ ] No privileged containers
* [ ] No unnecessary host mounts
* [ ] No Docker socket inside challenge containers
* [ ] Restricted networking where needed

---

## 8. First Complete Challenge

Start with one full room before creating more.

Possible first room:

```text
Linux Fundamentals
```

* [ ] Create challenge image
* [ ] Create room and tasks
* [ ] Launch challenge
* [ ] Complete tasks
* [ ] Track progress
* [ ] Stop challenge
* [ ] Test full workflow

Done when:

> One room works completely from start to finish.

---

## 9. Extra Features

Only after the core system works.

* [ ] Search rooms
* [ ] Filtering
* [ ] Dashboard
* [ ] Better UI
* [ ] Recommendations
* [ ] More challenge rooms

Possible rooms:

* Linux Fundamentals
* Networking Fundamentals
* HTTP Fundamentals
* Web Enumeration
* File Permissions
* Weak Authentication
* Log Analysis
* Basic Cryptography

---

## Workflow

For each feature:

```text
Choose feature
    ↓
Design it
    ↓
Add tests
    ↓
Implement
    ↓
Run checks
    ↓
Manual test
    ↓
Update NEA notes
    ↓
Commit
```

Keep commits small and specific.

Good:

```text
Add room model
Add flag validation
Add progress tracking
Add prerequisite cycle detection
```

Bad:

```text
stuff
changes
big update
```

---

## Current Focus

## Working On

* [ ] Accounts

## Next

* [ ] Registration/login
* [ ] Profile page
* [ ] Room model
* [ ] Task model

## Blocked

Nothing currently.

---

## MVP

The core project is complete when:

* [ ] Users can register/login
* [ ] Rooms and tasks work
* [ ] Answers can be checked
* [ ] Progress saves
* [ ] Scores work
* [ ] Prerequisites work
* [ ] Leaderboard works
* [ ] One Docker challenge launches
* [ ] One full room works end-to-end
* [ ] Core functionality is tested
* [ ] All checks pass
