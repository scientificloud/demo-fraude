
$( "#txt_causa" ).keypress(function( event ) {
    var str = $("#txt_causa").val();
    if(str.toLowerCase().indexOf("furto") >= 0 || str.toLowerCase().indexOf("roubo") >= 0 || str.toLowerCase().indexOf("assalto") >= 0){
        $("#caso_furto").show("slow")
    }
    else{
        $("#caso_furto").hide("slow")
    }

    if(str.toLowerCase().indexOf("natureza") >= 0 || str.toLowerCase().indexOf("fenômenos") >= 0 || str.toLowerCase().indexOf("fenomenos") >= 0){
        $("#caso_natureza").show("slow")
    }
    else{
        $("#caso_natureza").hide("slow")
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});