# WA3 Computing Project
How our project works:\
Main files:\
pc_main.py (runs the display on the pc)\
serial_connection.py (connects the pc to the microbit using pyserial)\
microbit_main.py (runs the microbit)\
Modules:\
module1_tables.py\
module2_crowds.py\
module3_queue.py\
module4_priority.py\
Other files:\
distance.py (for ultrasonic distance sensor)\
project_flowchart.md (flowchart of problem decomposition)\
tests.py (testcases including normal, boundary, error test cases)

# Setting up the project
## First-time setup (refer to how_to_use_requirements.txt)
1. Clone the repository.
2. Create a virtual environment:
   python -m venv .venv

3. Activate it:
   .\.venv\Scripts\Activate

4. Install dependencies:
   python -m pip install -r requirements.txt

## Running the project

PC program:
python pc_main.py

Flash the micro:bit:
uflash microbit_main.py
ufs put distance.py  -> to run the ultrasonic distance sensor to run the fan
