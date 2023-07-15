from fastapi import FastAPI

import bot
import send_sms

app = FastAPI()

@app.get("/decoder/{item_id}")
async def read_item(item_id: str):
    results = bot.generate_permutations(item_id)
    stringified_results = ' '.join(results)
    send_sms.sendText(stringified_results)
    return {"item_id": stringified_results}