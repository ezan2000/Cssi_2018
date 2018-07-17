// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;

function openAccount(name, balanceStart){
  balance = balanceStart;
  // Set the value for customer_name equal to name below
customer_name = name;
balance = 0;
  enter = `${customer_name} has opened a new account with a balance of $` + balance;
  return enter;  //write the statment you need to return here
}

function deposit(customer_name, value = 0){
balance = balance + value;
  // update the value of balance

  print = `${customer_name} has deposited ` + value;
  print2 = `${customer_name}'s total balance is ` + balance;
  return print;
  return print2;   //return the correct statement
}

function withdraw(customer_name, value = 0){
  //update the value of balance
  balance = balance - value;

print3 = `${customer_name}'s total balance is ` + balance;
print4 = `${customer_name}'s has withdrawn ` + value;
return print4;
return print3;
  //return the correct statement
}

// Write your script below
