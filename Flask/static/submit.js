$( "#btn_cadastrar_dados" ).click(function() {
    // var dados = JSON.stringify( $("#form_dados_cadastro").serializeArray() );
    // var dados = $('#form_dados_cadastro').serialize();


    var config = {};
    jQuery("#form_dados_cadastro").serializeArray().map(function(item) {
        if ( config[item.name] ) {
            if ( typeof(config[item.name]) === "string" ) {
                config[item.name] = [config[item.name]];
            }
            config[item.name].push(item.value);
        } else {
            config[item.name] = item.value;
        }
    });

    console.log(config)

    var jqxhr = $.post( "http://35.227.122.84:8080/cadastrar_dados", config ,  function(data) {
        console.log(data);
        alert(data.Resultado.Modelo.Mensagem);
    })
    .fail(function(data ) {
        alert( "error" );
    });
});