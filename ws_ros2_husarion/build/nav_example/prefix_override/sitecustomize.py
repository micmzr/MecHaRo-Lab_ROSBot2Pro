import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mmazur/Prace/MecHaRo-Lab_ROSBot2Pro/ws_ros2_husarion/install/nav_example'
