import pandas as pd
import numpy as np

conditions_list = [
  (condition1),
  (condition2),
  ....]

choices_list = [
  to_apply_when_condition1,
  to_apply_when_condition2,
  ...]

df['new_column'] = np.select(condiitons_list,choices_list, default=to_apply_when_not_in_conditions_list)
