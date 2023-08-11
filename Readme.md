#### Steps to run this application locally
1. Clone this repository in to your local machine
```bash
git clone <url>
```
2. Make sure that python is installed in your machine
```bash
python --version
```
3. Create a Virtual Enviromrent
```bash
virtualenv <name_of_your_env>
```
4. Activate virtual environment 
```bash 
.\<name_of_your_env>\Scripts\activate
```
5. Install all packages 
```bash 
pip install -r requirements.txt
```
6. Your server will run on http://127.0.0.1:5000/
7. Import [Postman collection](CoRider.postman_collection.json) in postman.
8. Run all requests.

Routes
1. POST http://127.0.0.1:5000/users feild= {name , email ,password}