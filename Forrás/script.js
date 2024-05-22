document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
    document.getElementById('element-one').dblclick=function(){

    }
    //box-shadow
    const elementTwo = document.getElementById('element-two');
    document.getElementById('element-two').onmouseover = function() {
        Object.style.boxShadow= "none"
      }
    // element-three: Kattintásra eltűnik
    const elementThree = document.getElementById('element-three');
      document.getElementById('element-three').onclick=function(){

      }
    // element-four: Kattintásra a háttere zöld lesz
    const elementFour = document.getElementById('element-four');
    document.getElementById("element-four").onclick=function(){
        this.style.backgroundColor="green"
    }
});