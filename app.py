# app.py
import os
from controllers.mutant_controller import app
from database.db_connection import initialize_database


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)