function atjaunotIetvaru(which) {
 document.getElementById("lapas_saturs").innerHTML = '<'+'object id="lapas" type="text/html" data="'+which.href+'"></'+'object>';
}

window.onload =function() {
  zimetuzcanvas();
}
function zimetuzcanvas() {
var canvas = document.getElementById("zimejums"); 
var konteksts= canvas.getContext("2d");
konteksts.fillStyle = "green";
konteksts.fillRect(20, 25, 100, 100);
  
}

function taisni() {
var canvas = document.getElementById("zimejums");
var ctx = canvas.getContext("2d");
ctx.strokeStyle = "purple";
ctx.strokeRect(60, 65, 100, 100);
  
}
function aplis() {
var canvas = document.getElementById("zimejums");
var konteksts = canvas.getContext("2d");
konteksts.beginPath();
konteksts.arc(200, 200, 50, 0, 2 * Math.PI)
  konteksts.lineWidth = 13;
  konteksts.fillStyle = "yellow";
  konteksts.strokeStyle = "red";
  konteksts.fill();
  konteksts.stroke();
}
function linija() {
var canvas = document.getElementById("zimejums");
var konteksts = canvas.getContext("2d");
  konteksts.beginPath();
  konteksts.moveTo(20, 20);
  konteksts.lineTo(60, 60);
  konteksts.lineWidth =5;
  konteksts.strokeStyle = "blue";
  konteksts.stroke();
}
function text() {
  var canvas = document.getElementById("zimejums");
  var konteksts = canvas.getContext("2d");
    konteksts.font = "30px Arial";
    konteksts.fillStyle = "black";
    konteksts.fillText("Sveiki, pasaule!", 75, 100)
    konteksts.lineWidth = 5;

}

function aprekins() {
let vards = document.getElementById("vards").value;
let pirmais= parseFloat(document.getElementById("a").value);
let otrais= parseFloat(document.getElementById("b").value);
 let summa= pirmais+otrais;
console.log("Tevi sauc:" + vards + " + Atbilde ir:" + summa);
document.getElementById("rezultats").innerHTML = "Tevi sauc:" + vards + " <br> Tu ievadiji a vertibu:" + pirmais + "<br> un otra vertiba: " + otrais + "<br> Atbilde ir:" + summa;
}

 let age =18;
 
if (age < 18) {
  console.log("Nepilngadīgs");
} else if (age >= 18 && age < 65) {
  console.log("Pilngadīgs");
} else {
  console.log("Pensionārs");
}

for(let i=0; i<=10; i++) {
  console.log(i);
  if (i==5) {
  console.log("Cipars ir pieci");
  }
}

let j=0;
while (j<=10) {
  console.log("Vertibas: " + j);
  j++;
}
  
let k=8;

do {
  console.log("DO WHILE: " + k);
  k++;
} while (k<=10) 
  
let skaitlis =[6,3,6,31,78,9];

for(let i=0; i<skaitlis.length; i++) {
  console.log(skaitlis[i]);
  if (i==2) {
    console.log("ir");
  }
  if (skaitlis[i] ==31) {
    console.log("IRRR")
  }
}
   

    

  

