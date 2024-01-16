from taskmanager import db


class Category(db.Model):
    # schema for a Category model
    # # db.Integer - specifies the data type for a column
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # 25 is the number of characters that can be put into this column.
    # Here's is 25 character string column
    # nullable means it's not empty or blank
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    # backref - Category references itself but in lwoer case now.

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for a Task model
    id = cb.Colun(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "cattegory.id", ondelete="CASCADE"), nullable=False)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )

#test test