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

let currentlily = 1;

let frogger = document.querySelector('#frog');

frogger.addEventListener('click', function(){
// Insert what should happen when you click on the frog!
console.log("hop!");



});
frogger.addEventListener('click', e=>{
  frogger.style.left = "33.5%";
  frogger.style.up = "15%"; 

});
