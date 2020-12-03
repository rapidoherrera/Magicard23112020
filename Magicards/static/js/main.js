$(document).ready(function(){
    $('.menu').click(function(){
        $('nav ul').toggleClass('active')
    })
})

$(document).ready(function(){
    $('.icon-bici').click(function(){
        $('#arri_cont').toggleClass('block')
    })
})

$(document).ready(function(){
    $('.btn_cancelar').click(function(){
        $('#arri_cont').removeClass('block')
    })
})

$(document).ready(function(){
    $('.btn_arriendo').click(function(){
        $('#arri_cont').removeClass('block')
        $('.en-curso').toggleClass('block')
        $('.icon-bici').toggleClass('none');
        var fec = document.getElementById('fecha-ini');
        var dat = new Date();
        var dia = dat.getDate();
        var mes = dat.getMonth()+1;
        var año = dat.getFullYear();
        var hora = dat.getHours();
        var min = dat.getMinutes();
        var sec = dat.getSeconds();
        fec.innerText="Fecha Inicio: "+dia+"/"+mes+"/"+año+" - "+hora+":"+min+":"+sec;
    })
})

$(document).ready(function(){
    $('.btn_finalizar').click(function(){
        $('.btn_finalizar').toggleClass('none');
        $('.btn_salir').toggleClass('visible');
        var fec_ter = document.getElementById('fecha-ter');
        var dat = new Date();
        var dia = dat.getDate();
        var mes = dat.getMonth()+1;
        var año = dat.getFullYear();
        var hora = dat.getHours();
        var min = dat.getMinutes();
        var sec = dat.getSeconds();
        fec_ter.innerText="Fecha Termino: "+dia+"/"+mes+"/"+año+" - "+hora+":"+min+":"+sec;
    })
})

$(document).ready(function(){
    $('.btn_salir').click(function(){
        var fec = document.getElementById('fecha-ini');
        var fec_ter = document.getElementById('fecha-ter');
        $('.icon-bici').removeClass('none');
        $('.en-curso').removeClass('block');
        $('.btn_finalizar').removeClass('none');
        $('.btn_salir').removeClass('visible');
        fec.innerText = "";
        fec_ter.innerText = "";
    })
})