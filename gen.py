import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Configuration
num_rows = 5000
business_units = ['Retail Banking', 'Corporate Banking', 'Wealth Management', 'Investment Banking', 'Credit Cards']
issue_types = ['KYC', 'AML', 'Sanctions', 'Fraud', 'Transaction Monitoring']
risk_levels = ['High', 'Medium', 'Low']
remediation_statuses = ['Open', 'In Progress', 'Closed']

data = []

for _ in range(num_rows):
    issue_id = f"ISSUE-{fake.unique.random_int(min=10000, max=99999)}"
    bu = random.choice(business_units)
    issue_type = random.choice(issue_types)
    risk = random.choice(risk_levels)
    
    # Generate dates
    days_open = random.randint(1, 120)
    date_opened = datetime.now() - timedelta(days=days_open)
    
    # Assign SLA limits based on Risk Level (High=15 days, Med=30 days, Low=60 days)
    if risk == 'High':
        sla_limit = 15
    elif risk == 'Medium':
        sla_limit = 30
    else:
        sla_limit = 60
        
    sla_status = 'Breached' if days_open > sla_limit else 'On-Track'
    status = random.choice(remediation_statuses)
    
    # If closed, fix the days open to not be breached as often
    if status == 'Closed':
        days_open = random.randint(1, sla_limit + 5)
        sla_status = 'Breached' if days_open > sla_limit else 'On-Track'

    data.append([issue_id, bu, issue_type, risk, date_opened.strftime('%Y-%m-%d'), days_open, sla_limit, sla_status, status])

# Export to CSV
df = pd.DataFrame(data, columns=['Issue_ID', 'Business_Unit', 'Issue_Type', 'Risk_Level', 'Date_Opened', 'Days_Open', 'SLA_Limit', 'SLA_Status', 'Remediation_Status'])
df.to_csv('financial_crimes_governance_logs.csv', index=False)
print("Dataset generated successfully!")