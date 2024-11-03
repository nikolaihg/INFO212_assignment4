# UTILS: 
def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

class DatabaseSession:
    def __init__(self, driver, dry_run=False):
        self.driver = driver
        self.dry_run = dry_run
        self.session = None
        self.transaction = None

    def __enter__(self):
        self.session = self.driver.session()
        self.transaction = self.session.begin_transaction()
        return self.transaction

    def __exit__(self, exc_type, exc_value, traceback):
        if self.dry_run or exc_type:
            self.transaction.rollback()
            print("Dry run or error: changes rolled back.")
        else:
            confirm = input("You are about to commit changes. Type 'yes' to confirm: ")
            if confirm.lower() == 'yes':
                self.transaction.commit()
                print("Changes committed.")
            else:
                self.transaction.rollback()
                print("Confirmation failed: changes rolled back.")
        self.session.close()