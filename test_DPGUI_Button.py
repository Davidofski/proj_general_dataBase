from datetime import datetime
import settings as st

x_datetime = datetime.now()
print("x_datetime:", x_datetime)

x_date = x_datetime.replace(microsecond=0, second=0, minute=0, hour=0)
print("x_date: ", x_date)

x_date = x_date.date()
print("x_date after change:", x_date)

y = st.item1_xpos
print(y)

input_date = {'sec': 0, 'min': 0, 'hour': 0, 'month_day': 1, 'month': 0, 'year': 122, 'week_day': 6, 'year_day': 0, 'daylight_savings': 0}
print("From input date [year]: ", input_date['year'])