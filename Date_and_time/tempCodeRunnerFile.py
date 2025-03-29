#Python DateTime Formatting
# --datetime to string
from datetime import datetime
dt = datetime.now()
datetime_str = dt.strftime("%d/%m/%Y %H:%M:%S")
print('DateTime String:', datetime_str)