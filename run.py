import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

# The __name__ is a built-in special variable that evaluates the
#  name of the current module.
# If the source file is executed as the main program,
# # the interpreter sets the __name__ variable to have a value “__main__”.
# If this file is being imported from another module, __name__ will be set
# to the module’s name.
