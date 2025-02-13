## Methodology
1. Natural language query to from whatsapp to backend via twilio.
2. Convert Natural language query to relavant sql query using LLM.
3. Hit Postgres with the sql.
4. Use recieved Data as context, along with user query to LLM.
5. Get Natural Language Response.
   
## API Reference

#### Get all items

```http
  POST /whatsapp
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `body` | `string` |  Singular CRUD API for expense tracking via whatsapp |


