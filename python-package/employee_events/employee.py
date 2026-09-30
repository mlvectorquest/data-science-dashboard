# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
# (QueryBase already mixes in QueryMixin, so self.query/self.pandas_query
# are available on Employee without a separate import here)

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):

        # Query 3
        # Write an SQL query
        # that selects two columns
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        return self.query(f"""
            SELECT first_name || ' ' || last_name, {self.name}_id
            FROM {self.name}
        """)


    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):

        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        return self.query(f"""
            SELECT first_name || ' ' || last_name
            FROM {self.name}
            WHERE {self.name}.{self.name}_id = {id}
        """)


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):

        return self.pandas_query(f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """)
