from neo4j import GraphDatabase

class Config:
    NEO4J_URI = "neo4j+s://71ccb90d.databases.neo4j.io"
    NEO4J_USERNAME = "neo4j"
    NEO4J_PASSWORD = "LyH6DFMZfG-p4YIqS8jln8Hcfpx-OnYJ_0WUs16DCXU"

def get_neo4j_driver():
    driver = GraphDatabase.driver(
        Config.NEO4J_URI,
        auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
    )
    return driver

def read_data(driver):
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 10")  # Example read query
        for record in result:
            print(record)

if __name__ == "__main__":
    print("NEO4J_URI:", Config.NEO4J_URI)
    print("NEO4J_USERNAME:", Config.NEO4J_USERNAME)
    print("NEO4J_PASSWORD:", Config.NEO4J_PASSWORD)

    driver = get_neo4j_driver()
    read_data(driver)
    driver.close()
