# RO-Crate Microservice Demo

This project demonstrates a basic microservice for managing Research Objects – Crates (RO-Crates) using Python, Flask and MongoDB.

## Introduction

RO-Crates are a structured way to package research data and their metadata, promoting reproducibility and reusability. This microservice provides the following core functionalities:

* **Create RO-Crates:** Store new RO-Crates with basic metadata in a MongoDB database.
* **Retrieve RO-Crates:** Fetch RO-Crates by their unique IDs.
* **Update RO-Crates:** Modify the metadata of existing RO-Crates.
* **Delete RO-Crates:** Remove RO-Crates from the database.

## Requirements

* **Python 3.7+** 
* **Flask** 
* **PyMongo** 


## Installation

**1. Clone the repository:**
   ```bash
   git clone https://github.com/Karanjot786/Demo_RO_Crate
   cd Demo_RO_Crate
   ```

**2. Create a virtual environment:**

   ```bash
    virtualenv env
    source env/bin/activate
   ```

**3. Install dependencies:**
   ```bash
    pip install -r requirements.txt
   ```
**3. Running the app**
   ```bash
    python app.py 
   ```
## Configuration

**1. MongoDB Connection:**

Create a *.env* file in the project's root directory.
Add the following variable, replacing the placeholder with your MongoDB connection string:


   ```bash
    MONGODB_URI=mongodb+srv://<username>:<password>@<your-cluster-address>/?retryWrites=true&w=majority
   ```

## API Endpoints

**1. POST /rocrate**

* Creates a new RO-Crate
* Request Body (JSON): 

   ```json
        {
            "title": "My RO-Crate",
            "description": "A research dataset",
            "author": "Your Name"
        }
   ```



**2. GET /rocrate/<rocrate_id>**

* Retrieves an RO-Crate by its ID.


**3. PUT /rocrate/<rocrate_id>**

* Updates an existing RO-Crate.



**4. DELETE /rocrate/<rocrate_id>**
   
* Deletes an RO-Crate.

## Working with CURL

**1. Create a new RO-Crate:**
   ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "My RO-Crate", "description": "A research dataset", "author": "Karanjot Singh}' http://localhost:5000/rocrate 
   ```

**2. Retrieve an RO-Crate:**
   ```bash
    curl http://localhost:5000/rocrate/<rocrate_id>  # Replace <rocrate_id> with an actual ID
   ```

**3. Update an RO-Crate:**
   ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Title", "description": "Modified description..."}'  http://localhost:5000/rocrate/<rocrate_id>  
   ```

**4. Delete an RO-Crate:**
   ```bash
    curl -X DELETE http://localhost:5000/rocrate/<rocrate_id>   
   ```


## THANKS