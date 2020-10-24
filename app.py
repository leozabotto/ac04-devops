import os
from flask import Flask, jsonify, request

fibo = Flask(__name__)

@fibo.route('/')
def fibonacci():
  prev_value = 1
  next_value = 0
  limit = 51
  found = 0
  response = "0,"
  while (found < limit):
      tmp = next_value
      next_value = next_value + prev_value
      prev_value = tmp
      found=found+1
      response += str(next_value) + ","


  return response

if __name__== "__main__":
    port = int(os.environ.get("PORT", 5001))
    fibo.run(host='0.0.0.0', port=port)
