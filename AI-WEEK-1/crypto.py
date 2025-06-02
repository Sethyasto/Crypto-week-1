# 📌 Crypto Advisor Chatbot: Week 1 Assignment
# Name: CryptoBuddy 🌟 Your First AI-Powered Financial Sidekick!

# 🧠 Chatbot Introduction
print("👋 Hey there! I’m CryptoBuddy — your friendly crypto sidekick! 💸")
print("Ask me about trending coins, sustainability, energy use, or profitability.")
print("Type 'help' to see what I can do. Type 'bye' to exit.\n")

# 💾 Predefined Cryptocurrency Dataset
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# 🤖 Chatbot Logic Function
def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"✅ Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        rising_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"📈 These coins are trending up: {', '.join(rising_coins)}")

    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                print(f"🚀 {name} is trending up and has a top-tier sustainability score!")

    elif "most profitable" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"💸 {name} is currently the most profitable based on trend and market cap.")

    elif "least energy" in user_query or "low energy" in user_query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        print(f"🔋 These coins use the least energy: {', '.join(low_energy)}")

    elif "energy use" in user_query:
        print("🔌 Crypto Energy Use:")
        for name, data in crypto_db.items():
            print(f"• {name}: {data['energy_use']} energy")

    elif "sort" in user_query or "rank" in user_query:
        sorted_coins = sorted(crypto_db.items(), key=lambda item: item[1]["sustainability_score"], reverse=True)
        print("📊 Coins ranked by sustainability:")
        for name, data in sorted_coins:
            print(f"{name} — Score: {data['sustainability_score']*10}/10")

    elif "stable" in user_query:
        stable = [name for name, data in crypto_db.items() if data["price_trend"] == "stable"]
        print(f"🪙 These coins are stable in price: {', '.join(stable)}")

    elif "help" in user_query or "what can you do" in user_query:
        print("🤖 I can answer questions about:\n"
              "- 🌱 Most sustainable crypto\n"
              "- 🔋 Coins using the least energy\n"
              "- 📈 Trending/upward coins\n"
              "- 🪙 Stable coins\n"
              "- 💸 Most profitable options\n"
              "- 📊 Sort coins by sustainability\n"
              "- Type 'bye' to exit\n")

    elif "bye" in user_query:
        print("👋 Thanks for chatting! Remember: Crypto is risky—always do your own research! 🔍")
        return False

    else:
        print("❓ I'm not sure about that. Try asking about sustainability, energy use, stable coins, or profitability.")
    
    return True

# 🔁 Chat Loop
chatting = True
while chatting:
    user_input = input("\nYou: ")
    chatting = respond_to_query(user_input)
