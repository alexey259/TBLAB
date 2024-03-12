import telebot
import config
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Функции для генерации нового адреса и получения баланса кошелька
def generate_new_address():
    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("rpc_username", "rpc_password"))
        new_address = rpc_connection.getnewaddress()
        return new_address
    except JSONRPCException as json_exception:
        return "An error occurred: " + str(json_exception)

def get_wallet_balance():
    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("rpc_username", "rpc_password"))
        balance = rpc_connection.getbalance()
        return str(balance)
    except JSONRPCException as json_exception:
        return "An error occurred: " + str(json_exception)

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['getnewaddress'])
def send_new_address(message):
    new_address = generate_new_address()
    bot.send_message(message.chat.id, new_address)

@bot.message_handler(commands=['getbalance'])
def send_balance(message):
    balance = get_wallet_balance()
    bot.send_message(message.chat.id, balance)

# RUN
bot.polling(none_stop=True)