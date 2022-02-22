# shopping-cart

## Installation
Clone the repo and navigate to it from the command line.
```sh
cd ~/Desktop/shopping-cart 
```

## Create a .env file
Set up your own env file. Create a file called .env and store the tax rate in a variable.

```sh
 # this is the ".env" file...
 
 TAX_RATE=0.0875
```

Sign up for a SendGrid account, then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account.
Create a SendGrid API key. Permissions must be "full access."
In a .env file, create an environment variable SENDGRID_API_KEY and store value in there. Then create another environment variable called SENDER_ADDRESS. This should be the email you used for your SendGrid account.

## Create a new environment
```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt
```

## Usage
Run the program:
```sh
python shopping_cart.py
```