## Idea Submission to Trufides AI
1. Natural Language based Expense Tracker
2. Add a expense of rs 250 for ola I took to work
   Processes Query and adds into Db.
   ![image](https://github.com/user-attachments/assets/16ac6e2d-6c84-47af-970e-740db64c2f76)

4. What is my total expense this month?
   Processes query, find relavant data rows and returns a natural response with total.
   
   ![image](https://github.com/user-attachments/assets/5fddf3c1-7641-404d-886f-1c96b0160a2f)
5. Categorical Search --> How much did I spend on food this month?
   Processes query, find categorically correct rows and returns a breakdown in natural language with total.
   ![image](https://github.com/user-attachments/assets/ca0a6c76-d829-4a45-94e7-bcd50e135878)



## Methodology/Pipleline
1. Natural language query to from whatsapp to backend via twilio.
2. Convert Natural language query to relavant sql query using LLM.
3. Hit Postgres with the sql query.
4. Use recieved Data as context, along with user query to LLM.
5. Get Natural Language Response.
   
## API Reference

#### Get Response Chat

```http
  POST /whatsapp
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `body` | `string` |  Singular CRUD API for expense tracking via whatsapp |


