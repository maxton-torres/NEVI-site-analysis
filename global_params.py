WALK_DIST = 500  # Distance in meters
WALK_DIST_MILE = WALK_DIST/1609.34
MILES_PER_METER = 1/1609.34

# Given the 20 minute minimum to charge most EVs using the NEVI-funded fast chargers, I recommend changing the WALK_DIST variable to 800 meters, which is about half a mile.

REPO_PATH = '/Users/sampackman/Documents/ev_charging_analysis'

import sys
sys.path.insert(0, REPO_PATH)
  # Latitude, Longitude of the center point
# Define the center point and the walking distance
