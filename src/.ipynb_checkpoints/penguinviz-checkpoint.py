import pandas as pd
import altair as alt
from palmerpenguins import load_penguins

penguins = load_penguins()
penguins.head()

plot = alt.Chart(
    data = penguins   
).encode(
    x = "flipper_length_mm",
    y = "body_mass_g"
).mark_point()

plot