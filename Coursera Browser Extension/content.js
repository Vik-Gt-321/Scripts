if(window.location.href.includes('coursera.org', '/lecture/'))
{
console.log("Entered if statement")
button = document.getElementsByClassName("rc-PlayToggle")
document.onkeydown = function(e) 
{
    if (e.altKey && e.ctrlKey) 
    {
        button[0].click()
        // alert("altKey + Ctrl combination was pressed");
    } 
}

}
else{
    console.log("Did not enter")
}
