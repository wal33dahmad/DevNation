window.addEventListener('scroll' , function(e){
 var opacity =  e.target.scrollingElement.scrollTop/400;
 var totalScroll = 400;

 document.getElementById('nav').style.background = "linear-gradient(rgba(31, 32, 51,"+opacity+"),rgba(24, 25, 40,"+opacity+"))";
    
})