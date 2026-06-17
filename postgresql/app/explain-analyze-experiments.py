from sqlalchemy import text
from jobs_500k import get_db_engine, create_index_on_salary

# Test connection
def is_engine_up() -> bool:
    my_engine = get_db_engine()
    try:
        with my_engine.begin() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Connection to database successful! ✅✅🚀")
            # Print out the result rows properly
            for row in result:
                print(row)
            return True
    except Exception as ex:
        print(f"❌❌❌ Failed to connect due to the error:\n{str(ex).splitlines()[0]}")
        return False
    
def top_20_jobs():
    if not is_engine_up():
        print("❌❌❌ Failed to connect! Server error")
        return None
    my_engine = get_db_engine()
    with my_engine.begin() as conn:
        print("Connection successful!✅✅✅")
        results = conn.execute(text("""
                    EXPLAIN ANALYZE
                    SELECT * FROM jobs
                    WHERE salary > 150000
                    ORDER BY salary DESC
                    LIMIT 20;
                """))
        return results

def experiment_results_withot_index():
    results = top_20_jobs()
    if not results:
        print("❌❌No results! Please check your environment file")
        return
    planning_time = ""
    execution_time = ""
    
    for row in results:
        line: str = row[0].strip()
        if line.startswith("Planning Time:"):
            planning_time = line
        elif line.startswith("Execution Time:"):
            execution_time = line
    
    with open("../notes/experiments-explain-analyze.md", 'w') as outputfile:
        print("Connection successful!!✅✅✅\nNow writing to an MD file...")
        
        outputfile.write("# Date: June 16, 2026\n")
        outputfile.write("# Objective/Goal:\n```\nTo Analyze Query Performance with EXPLAIN ANALYZE on 500k postgreSQL rows of data.\n```\n ")
        outputfile.write("## Experiment 1:\n```\nNo Index on salary column:\n```\n\n")
        outputfile.write("METRICS:\n")
        outputfile.write(f"```\n{planning_time}\n{execution_time}\n```\n\n\n")
   
        print("Done writing experiments to MD file!!\nBye😊😊😊")
    
# experiment_results_withot_index() # DONE ✅✅✅

def experiment_results_with_index():
    # create the index on salary column
    create_index_on_salary()
    # get top 20 highest paying jobs
    results = top_20_jobs()
    if not results:
        print("❌❌No results! Please check your environment file")
        return
    
    planning_time = ""
    execution_time = ""
    
    # get the needed data from the query
    for row in results:
        line: str = row[0].strip()
        if line.startswith("Planning Time:"):
            planning_time = line
        elif line.startswith("Execution Time:"):
            execution_time = line   
    
    # write the results to a markdown/MD file
    with open("../notes/experiments-explain-analyze.md", 'a') as outputfile:
        print("Connection successful!!✅✅✅\nNow writing to an MD file...")
        
        outputfile.write("## Experiment 2:\n```\nIndex created on salary column:\n```\n\n")
        outputfile.write("METRICS:\n")
        outputfile.write(f"```\n{planning_time}\n{execution_time}\n```\n\n\n")
        
        # write a conclusion
        outputfile.write(f"CONCLUSION\n")
        outputfile.write(f"```\nWith no index on the salary column, query execution is slower. Adding an index can greatly improve query execution time.\n```")
        print("Done writing experiments to MD file!!\nBye😊😊😊")
         
experiment_results_with_index()
