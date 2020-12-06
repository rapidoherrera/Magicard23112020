window.onload = function carousel () {
    // Variables
    var myIndex = 0;
    carousel();

    function carousel() {
        // Activate Carousel
        $("#myCarousel").carousel({interval: 500});
            
        // Enable Carousel Indicators
        $(".item1").click(function(){
            $("#myCarousel").carousel(0);
        });
        $(".item2").click(function(){
            $("#myCarousel").carousel(1);
        });
        $(".item3").click(function(){
            $("#myCarousel").carousel(2);
        });
        $(".item4").click(function(){
            $("#myCarousel").carousel(3);
        });
            
        // Enable Carousel Controls
        $(".left").click(function(){
            $("#myCarousel").carousel("prev");
        });
        $(".right").click(function(){
            $("#myCarousel").carousel("next");
        });
        
    }
    
      
} 

function bigImg(x) {
    x.style.height = "500px";
    x.style.width = "250px";
}
  
  function normalImg(x) {
    x.style.height = "400px";
    x.style.width = "200px";
}

