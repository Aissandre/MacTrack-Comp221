# MacTrack-Comp221

## About the Project
MacTrack-Comp221 is a course planning utility designed to assist Computer Science majors in organizing their degree path. It uses Kahn's Algorithm to determine a valid order for taking courses based on prerequisites.

The program allows users to input a list of courses they plan to take. It then:
1.  **Builds a dependency graph** of courses and their prerequisites.
2.  **Checks for Major Requirements**: Automatically verifies if the core curriculum (e.g., COMP 123, 127, 128, 221, 225, 240, MATH 279) and elective requirements (Math/Stat electives, Advanced COMP electives, Capstone) are met.
3.  **Fills Gaps**: If requirements are missing, the system randomly selects valid courses to fulfill them.
4.  **Generates a Schedule**: Outputs a topologically sorted list of courses, ensuring prerequisites are taken before the courses that require them.

## Requirements
- The repository must be cloned to your local machine.
## How to Run

### In Git Bash (or Terminal)
1. Open your terminal or Git Bash.
2. Navigate to the project directory:
   ```bash
   cd path/to/MacTrack-Comp221
   ```
3. Run the main script using Python:
   ```bash
   python topologicalSort.py
   ```
   *(Note: Depending on your operating system, you may need to use `python3` instead of `python`)*.
4. When prompted, enter the course codes you wish to take, separated by commas (e.g., `COMP 127, COMP 221`).

### In an IDE
1. Open the **MacTrack-Comp221** project folder in your IDE.
2. Locate the `topologicalSort.py` file in the Project View.
3. Look for the **Run/Console** window at the bottom of the IDE.
4. Click inside the console to focus it, and type your desired courses when prompted.