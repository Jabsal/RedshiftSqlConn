from sqlalchemy import create_engin
import pandas
import matplotlib.pyplot as plt
 
engine = create_engine("redshift:///?User={REDSHIFT_USER}&;Password={REDSHIFT_PASSWORD}&Database={REDSHIFT_DATABASE}&Server={REDSHIFT_HOST}&Port={REDSHIFT_PORT}")
df = pandas.read_sql("select bookname, author from book", engine)
 
df.plot(kind="bar", x="bookname", y="author")
plt.show()
