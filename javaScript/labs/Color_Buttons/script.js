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

// Use querySelector to store the div in a variable.
let redButton = document.querySelector('#red');
let box = document.querySelector("#responseBox");
// Use addEventListener to respond to a click event.
redButton.addEventListener('click', e => {
  console.log("You clicked the red button!")
  box.style.backgroundColor = "red";
  box.innerText = (box.innerText + " red");
})
let green = document.querySelector('#green');
green.addEventListener('click', g => {

  console.log("You clicked the green button!")
  box.style.backgroundColor = "green"
  box.innerText = (box.innerText+ " green");
})
let blue = document.querySelector('#blue');
blue.addEventListener('click', b => {

  console.log("You clicked the blue button!")
  box.style.backgroundColor = "blue";
  box.innerText = (box.innerText + " blue")
})
let clear = document.querySelector("#clear");
clear.addEventListener('click', c => {
  box.style.backgroundColor = "white";
  box.innerText = ""; 
})
