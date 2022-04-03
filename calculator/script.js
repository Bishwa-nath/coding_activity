let = outputScreen = document.getElementById("output-screen")
let ok = false
function display(num){
    // To remove previous result
    if(outputScreen.value != null && ok){
        outputScreen.value = "";
    }
    if(ok == true){
        ok = false;
    }
    outputScreen.value += num
}
function calculate(){
    try{
        outputScreen.value = eval(outputScreen.value)
        ok = true;  // result is calculated
    }
    catch(err){
        alert("Invalid Input")
    }
}
function Clear(){
    outputScreen.value = "";
}
function del(){
    outputScreen.value = outputScreen.value.slice(0, -1);
}