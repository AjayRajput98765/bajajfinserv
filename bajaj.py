import requests

def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    headers = {"Content-Type": "application/json"}
    data = {
        "name": "Ajay Rajput",
        "regNo": "0827CA241003",
        "email": "ajayrajput98263@gmail.com"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        webhook_data = response.json()
        webhook_url = webhook_data['webhook']
        access_token = webhook_data['accessToken']
        print("Webhook URL:", webhook_url)
        print("Access Token:", access_token)
        return webhook_url, access_token
    else:
        print("Error in generating webhook:", response.text)
        return None, None

def solve_sql_problem(reg_no):
    last_digit = int(reg_no[-1])
    
    if last_digit % 2 == 0:
        print("Fetching Question 2...")
        sql_query = "SELECT * FROM users WHERE age > 30;"
    else:
        print("Fetching Question 1...")
        sql_query = "SELECT name, COUNT(*) FROM orders GROUP BY name;"
    
    return sql_query

def submit_solution(webhook_url, access_token, sql_query):
    url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    data = {
        "finalQuery": sql_query
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Solution submitted successfully!")
    else:
        print("Error in submitting solution:", response.text)

def main():
    webhook_url, access_token = generate_webhook()

    if webhook_url and access_token:
        reg_no = "0827CA241003"
        sql_query = solve_sql_problem(reg_no)

        submit_solution(webhook_url, access_token, sql_query)

if __name__ == "__main__":
    main()
