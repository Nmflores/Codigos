$(document).ready(function teste(){
        $(".brincadeira").click(function(){
        let valor1= $(this).text();
        let valor2=$(this).text()

        if(valor1 =="\u00A9Criado por Nicolas Machado Flores"){
            $(".brincadeira").text("\u00A9Criado por mim.")
        }
       if(valor2 =="\u00A9Criado por mim."){
           $(".brincadeira").text("\u00A9Criado por Nicolas Machado Flores");
       }
        
        })

        $("section p").click(function(){
            $("h1").text("Brincando com Jquery");

        })

});
