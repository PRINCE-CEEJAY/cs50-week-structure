# BlackBox: A Tamper-Evident Activity Logging System
    #### Video Demo:  <URL HERE>
    #### Description:
    🧱 MVP (Minimum Viable Project)

1️⃣ Append-Only Activity Logging

What it does
Records user-supplied actions/events
Stores them sequentially in a local file (JSON or text)

Why it matters
Introduces the concept of an audit log
Prevents silent overwrites

Technical signal
File I/O
Data serialization
Input validation

2️⃣ Hash-Chained Log Entries (Core Concept)

What it does
Each log entry includes:
timestamp
event description
hash of the previous entry

Why it matters
This is the heart of the project
Any modification breaks the chain

Technical signal
Cryptographic hashing
Deterministic functions
Conceptual depth without overengineering

3️⃣ Integrity Verification Mode

What it does
Scans the log file from start to end
Recomputes hashes
Detects and reports:
   tampered entries
   broken hash links
   malformed data

Why it matters
Shows defensive programming
Demonstrates trust verification

Technical signal
Algorithms
Error handling
Clear reporting

4️⃣ Clear CLI Interface

What it does
Accepts commands like:
   add (log an event)
   verify (check integrity)
   show (display entries)

Why it matters
Makes the project usable and demo-friendly
Demonstrates program flow and parsing

Technical signal
Argument handling
Program structure
User experience

5️⃣ Pytest Coverage for Core Logic

What it does
Tests at least 3 functions:
   hash computation
   log writing
   integrity verification

Why it matters
Required by CS50
Proves correctness

Technical signal
Professional discipline

Edge-case thinking
    TODO
