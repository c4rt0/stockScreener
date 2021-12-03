from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./stocks.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# # IN ORDER TO RUN THE SQLALCHEMY IN TERMINAL NAVIGATE TO LOCATION OD stocks.db FILE # #

# ```bash
#    sqlite3 stocks.db
# ```

# Once logged into the sqlite console:

# ```bash
#    select * from stocks;  --> displays all fields 
#    insert into stocks (symbol) values ('AAPL');  --> inserts AAPL into symbol
#    delete * from stocks; --> delets all entries from stocks.db
# ```