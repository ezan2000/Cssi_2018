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
let dogs = 0;
console.log(dataObject);
dataObject.data.forEach((element) =>  {
let url = element.images.original.url;
console.log(url);

}

)

const button = (document.querySelector('.button'));
button.addEventListener('click', b => {
  dataObject.data.forEach((element) => {
let url = element.images.original.url;
const img = document.createElement('img');
img.src = element.images.original.url;
img.width = '200';
img.height = '200';
var element = document.getElementById('body');
element.append(img);
  }
)
  // console.log(dataObject.data["0"].url);
  // const img = document.createElement('img');
  // img.src = dataObject.data["0"].images.original.url;
  // img.width = '200';
  // img.height = '200';
  // var element = document.getElementById('body');
  // element.append(img);
})
