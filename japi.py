import urllib.request
import json

def getStockData(stockSymbol):
    api = stockSymbol
    nasdaqAppleURL = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols="+api+"&apikey=8VGIPVX6AG66WE9V"
    connection = urllib.request.urlopen(nasdaqAppleURL)
    responseString = connection.read().decode()
    print(responseString)
    pd = json.loads(responseString)
    f = open("japi.out", "a+")
    f.write(responseString)
    f.write("The current price of " +api+" is "+pd['Stock Quotes'][0]['2. price'])
    f.close()
    print("Stock Quotes retrieved successfully!")

def main():
    while True:
        user_input = input("Please Enter a Stock Symbol: ")
        if user_input == "quit":
            break;
        else:
            getStockData(user_input)

if __name__ == "__main__":
    main()